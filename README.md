# E-commerce Customer Support Agent

An intelligent customer support automation system built with LangGraph and powered by Google Gemini 2.5 Flash Lite.

## Features

- **Intent Classification**: Automatically identifies customer issue types
- **Smart Routing**: Routes messages to appropriate handlers
- **Context-Aware Responses**: Generates helpful, contextual replies
- **Escalation Management**: Automatically escalates complex cases to human agents
- **Simple Web UI**: Clean, easy-to-use interface

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
├── main.py            # FastAPI application
├── templates/         # HTML templates
│   └── index.html
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variables template
└── README.md         # This file
```

## How It Works

The agent uses a multi-step workflow:

1. **Message Reception**: Customer message is received
2. **Intent Classification**: AI identifies the issue type
3. **Routing Decision**: Message is routed to appropriate handler
4. **Response Generation**: Context-aware response is generated
5. **Escalation Check**: Determines if human intervention is needed

## Technology Stack

- **LangGraph**: Workflow orchestration
- **Google Gemini 2.5 Flash Lite**: LLM for understanding and generation
- **FastAPI**: Backend API framework
- **Jinja2**: Template rendering for UI

## License

MIT License - See LICENSE file for details
