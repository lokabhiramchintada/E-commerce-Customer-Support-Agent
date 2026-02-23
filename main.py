"""
FastAPI backend for E-commerce Customer Support Agent
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
from agent import process_customer_message
import os
from datetime import datetime

app = FastAPI(
    title="E-commerce Customer Support Agent",
    description="AI-powered customer support automation with LangGraph",
    version="1.0.0"
)

# Setup templates
templates = Jinja2Templates(directory="templates")


class CustomerMessage(BaseModel):
    """Request model for customer messages"""
    message: str


class SupportResponse(BaseModel):
    """Response model for support agent"""
    response: str
    intent: str
    sentiment: str
    needs_escalation: bool
    confidence: float
    order_id: str | None
    timestamp: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main UI"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/support", response_model=SupportResponse)
async def handle_support_message(customer_message: CustomerMessage):
    """
    Process a customer support message through the AI agent
    
    Args:
        customer_message: Customer's message
        
    Returns:
        AI-generated response with metadata
    """
    try:
        # Validate message
        if not customer_message.message or len(customer_message.message.strip()) == 0:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        if len(customer_message.message) > 2000:
            raise HTTPException(status_code=400, detail="Message too long (max 2000 characters)")
        
        # Process through agent
        result = process_customer_message(customer_message.message)
        
        # Add timestamp
        result["timestamp"] = datetime.now().isoformat()
        
        return SupportResponse(**result)
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing message: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing message: {str(e)}")


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "customer-support-agent"
    }


@app.get("/api/intents")
async def get_supported_intents():
    """Get list of supported customer intent types"""
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


if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️  WARNING: GOOGLE_API_KEY not found in environment variables!")
        print("Please create a .env file with your API key:")
        print("GOOGLE_API_KEY=your_key_here")
        print("\nYou can copy .env.example to .env and update it.")
        exit(1)
    
    print("\n" + "="*70)
    print("🤖 E-commerce Customer Support Agent")
    print("="*70)
    print("\n✅ Starting server...")
    print("📍 Open your browser and navigate to: http://localhost:8000")
    print("\n💡 Press CTRL+C to stop the server\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
