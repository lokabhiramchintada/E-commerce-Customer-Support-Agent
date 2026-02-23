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
2. Type a customer message in the text area
3. Click "Send Message" or press Enter
4. View the AI-generated response and metadata

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

- `GET /` - Web UI
- `POST /api/support` - Process customer message
- `GET /api/health` - Health check
- `GET /api/intents` - List supported intent types

## Example Messages to Try

- "Where is my order #12345? It's been 2 weeks!"
- "I received a broken phone. This is unacceptable!"
- "Can I get a refund for order ORD-98765?"
- "How do I cancel my order before it ships?"
- "I was charged twice for the same order"
