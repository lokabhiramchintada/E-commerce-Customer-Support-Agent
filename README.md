# E-commerce Customer Support Agent

An intelligent customer support automation system powered by Google Gemini 2.5 Flash Lite.

This repository now contains **two implementations**:
- **True A2A implementation** (`A2A/`) - independent agents with explicit handoffs
- **Legacy LangGraph implementation** (`langgraph/`) - graph-orchestrated workflow

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

5. **Run one implementation**
   ```bash
   # True A2A (recommended)
   python A2A/main.py

   # Legacy LangGraph
   python langgraph/main.py
   ```

6. **Access the UI**
   - Open your browser and go to: `http://localhost:8000`

## 🐳 Docker Setup

You can also run the application using Docker:

### Pull from Docker Hub
```bash
docker pull abhisigningin/a2a-backend
```

### Run the container
```bash
docker run -d \
  --name a2a-backend \
  -p 8000:8000 \
  -e GOOGLE_API_KEY=your_api_key_here \
  abhisigningin/a2a-backend:latest
```

### Or use Docker Compose
```bash
# Create .env file with GOOGLE_API_KEY
docker-compose up -d
```

For detailed Docker setup instructions, see [DOCKER_SETUP.md](DOCKER_SETUP.md).

## Project Structure

```
.
├── A2A/
│   ├── agent.py       # Compatibility entrypoint (delegates to orchestrator)
│   ├── orchestrator.py # True A2A orchestration (plain Python handoffs)
│   ├── contracts.py   # Shared context contract between agents
│   ├── llm_client.py  # Shared Gemini client factory
│   ├── agents/
│   │   ├── intent_agent.py
│   │   ├── order_lookup_agent.py
│   │   ├── response_agent.py
│   │   └── escalation_agent.py
│   ├── data.py        # Dummy database (orders, products, customers)
│   └── main.py        # FastAPI application and API endpoints
├── langgraph/         # Legacy LangGraph-based implementation
│   ├── agent.py
│   ├── data.py
│   └── main.py
├── templates/         # HTML templates
│   └── index.html     # Web UI with sample data display
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
└── README.md          # This file
```

## 🆚 Two Implementations

### 1) True A2A (Recommended)
- Path: `A2A/`
- Model: independent agents with explicit context contract handoffs
- Orchestration: plain Python orchestrator (`A2A/orchestrator.py`)
- Run:
   ```bash
   python A2A/main.py
   ```

### 2) Legacy LangGraph
- Path: `langgraph/`
- Model: single graph workflow implementation
- Orchestration: LangGraph state graph
- Run:
   ```bash
   python langgraph/main.py
   ```

Both implementations expose the same API endpoints and serve the same UI at `http://localhost:8000`.

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

## How It Works (A2A)

The system now uses a **true A2A handoff model** with independent agents:

1. **Intent Agent**: Classifies issue type, sentiment, confidence, and order ID
2. **Order Lookup Agent**: Fetches matching order data from the dummy database
3. **Response Agent**: Generates customer reply using message + order context
4. **Escalation Agent**: Applies escalation rules for confidence/sentiment/urgency

The orchestrator passes a shared `SupportContext` contract between agents in sequence.

## How It Works (LangGraph - Legacy)

The legacy implementation uses a LangGraph state graph with node-based orchestration:

1. **classify_intent** node
2. **route_to_handler** node
3. **generate_response** node
4. **check_escalation** node

The graph is compiled and invoked as a single workflow execution in `langgraph/agent.py`.

## Technology Stack

- **A2A Workflow Layer**: Independent agents + explicit context handoffs
- **LangGraph (legacy path)**: Graph-based workflow orchestration in `langgraph/`
- **Google Gemini 2.5 Flash Lite**: LLM for understanding and generation
- **FastAPI**: Backend API framework
- **Jinja2**: Template rendering for UI

## Run from Workspace Root

Always run commands from the workspace root (`E-commerce-Customer-Support-Agent`) so `templates/` resolves correctly:

```bash
# True A2A
python A2A/main.py

# Legacy LangGraph
python langgraph/main.py
```

## License

MIT License - See LICENSE file for details
