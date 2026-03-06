"""
FastAPI backend for E-commerce Customer Support Agent (A2A)
"""

from datetime import datetime
import os

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

from agent import process_customer_message
from data import ORDERS, PRODUCTS, CUSTOMERS, get_order, get_order_summary

app = FastAPI(
    title="E-commerce Customer Support Agent",
    description="AI-powered customer support automation with A2A workflow",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")


class CustomerMessage(BaseModel):
    message: str


class SupportResponse(BaseModel):
    response: str
    intent: str
    sentiment: str
    needs_escalation: bool
    confidence: float
    order_id: str | None
    timestamp: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/support", response_model=SupportResponse)
async def handle_support_message(customer_message: CustomerMessage):
    try:
        if not customer_message.message or len(customer_message.message.strip()) == 0:
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        if len(customer_message.message) > 2000:
            raise HTTPException(status_code=400, detail="Message too long (max 2000 characters)")

        result = process_customer_message(customer_message.message)
        result["timestamp"] = datetime.now().isoformat()

        return SupportResponse(**result)

    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(exc)}")


@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "customer-support-agent"
    }


@app.get("/api/intents")
async def get_supported_intents():
    return {
        "intents": [
            {
                "type": "delivery_inquiry",
                "description": "Questions about shipping, tracking, delivery time"
            },
            {
                "type": "refund_request",
                "description": "Requests for money back, return requests"
            },
            {
                "type": "damaged_item",
                "description": "Reports of broken, defective, or damaged products"
            },
            {
                "type": "order_cancellation",
                "description": "Requests to cancel an order"
            },
            {
                "type": "payment_issue",
                "description": "Problems with payment, billing, charges"
            },
            {
                "type": "general_inquiry",
                "description": "General questions, account issues, other"
            }
        ]
    }


@app.get("/api/orders")
async def get_all_orders():
    return {
        "orders": list(ORDERS.values()),
        "total": len(ORDERS),
        "summary": get_order_summary()
    }


@app.get("/api/orders/{order_id}")
async def get_order_details(order_id: str):
    order = get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return order


@app.get("/api/products")
async def get_all_products():
    return {
        "products": list(PRODUCTS.values()),
        "total": len(PRODUCTS)
    }


@app.get("/api/customers")
async def get_all_customers():
    return {
        "customers": list(CUSTOMERS.values()),
        "total": len(CUSTOMERS)
    }


if __name__ == "__main__":
    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️  WARNING: GOOGLE_API_KEY not found in environment variables!")
        print("Please create a .env file with your API key:")
        print("GOOGLE_API_KEY=your_key_here")
        print("\nYou can copy .env.example to .env and update it.")
        raise SystemExit(1)

    print("\n" + "=" * 70)
    print("🤖 E-commerce Customer Support Agent (A2A)")
    print("=" * 70)
    print("\n✅ Starting server...")
    print("📍 Open your browser and navigate to: http://localhost:8000")
    print("\n💡 Press CTRL+C to stop the server\n")

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")