# Stock Analysis API

A FastAPI-based REST API for stock analysis and visualization.

## Features

- YTD stock price analysis
- Stock price visualization
- Modern FastAPI framework with automatic OpenAPI documentation
- Type hints and Pydantic models for request/response validation
- High performance with async support
- OpenAI integration for advanced analysis

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the following variables in `.env`:
     ```
     OPENAI_API_KEY=your-openai-api-key-here
     SECRET_KEY=your-secret-key-here  # Generate a secure key
     ```
   - You can generate a secure SECRET_KEY using:
     ```bash
     openssl rand -hex 32
     ```

4. Run the application:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
Interactive API documentation will be available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Environment Variables

The following environment variables can be configured in `.env`:

```ini
# API Configuration
API_V1_STR="/api/v1"
PROJECT_NAME="Stock Analysis API"
BACKEND_CORS_ORIGINS=["*"]

# Security
SECRET_KEY="your-secret-key-here"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# OpenAI Configuration
OPENAI_API_KEY="your-openai-api-key-here"
OPENAI_MODEL="gpt-4-turbo-preview"

# Other Settings
DEBUG=True
ENVIRONMENT="development"
```

## API Endpoints

### POST /api/v1/stocks/analysis
Analyze stocks and generate visualization

Request body:
```json
{
    "symbols": ["NVDA", "TSLA"]
}
```

### GET /api/v1/stocks/plot/{filename}
Get the generated plot image

## Example Usage

```python
import httpx
import asyncio

async def get_stock_analysis():
    async with httpx.AsyncClient() as client:
        # Get stock analysis
        response = await client.post(
            'http://localhost:8000/api/v1/stocks/analysis',
            json={'symbols': ['NVDA', 'TSLA']}
        )
        data = response.json()
        
        # View the plot
        plot_url = f"http://localhost:8000/api/v1/stocks/plot/{data['plot_path']}"
        return data, plot_url

# Run the async function
data, plot_url = asyncio.run(get_stock_analysis())
```

## Development

The project structure follows modern Python practices:

```
backend/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── stock_routes.py
│   ├── models/
│   │   └── stock_models.py
│   ├── utils/
│   │   └── stock_utils.py
│   ├── config.py
│   └── main.py
├── static/
│   └── plots/
├── .env
├── requirements.txt
└── README.md
``` 