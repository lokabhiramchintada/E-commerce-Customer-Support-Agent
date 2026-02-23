# E-commerce Customer Support Agent

An intelligent customer support automation system built with LangGraph and powered by Google Gemini 2.5 Flash Lite.

## ✨ Features

- **Intent Classification**: Automatically identifies customer issue types
- **Smart Routing**: Routes messages to appropriate handlers
- **Context-Aware Responses**: Generates helpful, contextual replies with real order data
- **Escalation Management**: Automatically escalates complex cases to human agents
- **Real Database Integration**: Includes dummy order/product/customer data for testing
- **Simple Web UI**: Clean, easy-to-use interface

## 🗃️ Dummy Data Available

The system includes a **complete dummy database** for realistic testing:

- **8 Sample Orders** (ORD-12345 through ORD-89012)
  - Various statuses: In Transit, Delivered, Processing, Shipped, Refund Requested, Cancelled
  - Real tracking numbers and delivery dates
  - Complete order details with products and prices
  
- **10 Products** (Electronics & Accessories)
  - Headphones, Smart Watches, Keyboards, Webcams, etc.
  - Pricing, stock levels, and ratings
  
- **5 Customers** with realistic profiles

**Try asking questions about real orders!** For example:
- "Where is my order ORD-12345?"
- "What's the status of order ORD-23456?"
- "I want to return order ORD-78901"

The AI agent will look up actual data and provide accurate, context-aware responses!

## Supported Issue Types

- Delivery inquiries
- Refund requests
- Damaged items
- Order cancellations
- Payment issues
- General inquiries

## Setup

1. **Clone the repository**
   ```bash
   cd E-commerce-Customer-Support-Agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   - Copy `.env.example` to `.env`
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the UI**
   - Open your browser and go to: `http://localhost:8000`

## Project Structure

```
.
├── agent.py           # LangGraph workflow and agent logic
├── data.py            # Dummy database (orders, products, customers)
├── main.py            # FastAPI application and API endpoints
├── templates/         # HTML templates
│   └── index.html     # Web UI with sample data display
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
└── README.md         # This file
```

## 🔌 API Endpoints

The application exposes several REST API endpoints:

### Support Agent
- `POST /api/support` - Send a customer message and get AI response
- `GET /api/intents` - List supported intent types

### Data Access
- `GET /api/orders` - Get all orders with summary
- `GET /api/orders/{order_id}` - Get specific order details
- `GET /api/products` - Get all products
- `GET /api/customers` - Get all customers
- `GET /api/health` - Health check

**Example API Usage:**
```bash
# Get all orders
curl http://localhost:8000/api/orders

# Get specific order
curl http://localhost:8000/api/orders/ORD-12345

# Send support message
curl -X POST http://localhost:8000/api/support \
  -H "Content-Type: application/json" \
  -d '{"message": "Where is my order ORD-12345?"}'
```

## How It Works

The agent uses a multi-step workflow:

1. **Message Reception**: Customer message is received
2. **Intent Classification**: AI identifies the issue type and extracts order ID
3. **Data Lookup**: System fetches real order data from database
4. **Routing Decision**: Message is routed to appropriate handler
5. **Response Generation**: Context-aware response is generated using real data
6. **Escalation Check**: Determines if human intervention is needed

## Technology Stack

- **LangGraph**: Workflow orchestration
- **Google Gemini 2.5 Flash Lite**: LLM for understanding and generation
- **FastAPI**: Backend API framework
- **Jinja2**: Template rendering for UI

## License

MIT License - See LICENSE file for details
