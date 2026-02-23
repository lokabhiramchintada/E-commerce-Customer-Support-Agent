# Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://ai.google.dev/))

## Installation Steps

### Windows
1. Run the setup script:
   ```cmd
   setup.bat
   ```

2. Edit `.env` file and add your API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

3. Start the server:
   ```cmd
   venv\Scripts\activate
   python main.py
   ```

### Linux/Mac
1. Make setup script executable and run it:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. Edit `.env` file and add your API key:
   ```bash
   nano .env
   # Add: GOOGLE_API_KEY=your_actual_api_key_here
   ```

3. Start the server:
   ```bash
   source venv/bin/activate
   python main.py
   ```

## Manual Installation

If you prefer manual setup:

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate (Windows)
venv\Scripts\activate
# Or (Linux/Mac)
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
copy .env.example .env  # Windows
# or
cp .env.example .env    # Linux/Mac

# 5. Edit .env and add your API key

# 6. Run the application
python main.py
```

## Using the Application

1. Open your browser to `http://localhost:8000`
2. **View Sample Orders**: The UI displays 6 sample orders you can ask about
3. Type a customer message or click an example button
4. Click "Send Message" or press Enter
5. View the AI-generated response with real order data and metadata

### 💡 Try These Questions with Real Data

The system includes 8 sample orders with complete details. Try questions like:

- **"Where is my order ORD-12345?"** - Get tracking info and delivery status
- **"What's the status of order ORD-23456?"** - Already delivered!
- **"I want to return order ORD-78901"** - Refund already in progress
- **"Cancel my order ORD-34567"** - Currently processing
- **"My order ORD-45678 hasn't arrived"** - Get tracking number

The AI agent will:
1. Extract the order ID from your message
2. Look up real order data from the database
3. Provide accurate, context-aware responses with specific details

### 🗃️ Available Sample Data

- **8 Orders** with various statuses (In Transit, Delivered, Processing, etc.)
- **10 Products** (Electronics & Accessories)
- **5 Customers** with order history

You can also access the data via API:
```bash
curl http://localhost:8000/api/orders
curl http://localhost:8000/api/orders/ORD-12345
```

## Testing the Agent Directly

You can also test the agent from command line:

```bash
python agent.py
```

This will run test messages through the workflow and display results.

## Troubleshooting

### "GOOGLE_API_KEY not found"
- Make sure you created the `.env` file
- Verify your API key is correctly set in `.env`
- Restart the application after editing `.env`

### Import errors
- Ensure you activated the virtual environment
- Run `pip install -r requirements.txt` again

### Port 8000 already in use
- Edit `main.py` and change the port number in `uvicorn.run()`
- Or stop the process using port 8000

## API Endpoints

### Support Agent
- `GET /` - Web UI
- `POST /api/support` - Process customer message
- `GET /api/intents` - List supported intent types

### Data Access
- `GET /api/orders` - Get all orders with summary
- `GET /api/orders/{order_id}` - Get specific order details  
- `GET /api/products` - Get all products
- `GET /api/customers` - Get all customers
- `GET /api/health` - Health check

## Example Messages to Try (With Real Order IDs!)

- "Where is my order ORD-12345? It's been 2 weeks!"
- "What's the status of order ORD-23456?"
- "I want to return the speaker from order ORD-78901"
- "Can I cancel order ORD-34567? I ordered by mistake"
- "My order ORD-45678 hasn't arrived yet"

**All these orders exist in the database and will return real data!**
