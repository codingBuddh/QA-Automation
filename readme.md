# AI-Powered Stock Analysis API 📈

A sophisticated FastAPI-based REST API that combines traditional stock analysis with AI-powered insights using AutoGen agents. This system provides comprehensive stock analysis, technical indicators, and market sentiment analysis.

## 🌟 Features

- **Advanced Stock Analysis**
  - Year-to-date (YTD) performance tracking
  - Technical indicators (RSI, MACD, Moving Averages)
  - Interactive price visualizations
  - Historical data analysis

- **AI-Powered Insights**
  - Market sentiment analysis
  - Automated technical analysis
  - Trend predictions
  - News sentiment integration

- **Modern Architecture**
  - FastAPI for high-performance async operations
  - AutoGen agents for intelligent analysis
  - Pydantic for robust data validation
  - Swagger/OpenAPI documentation
  - Type hints and modern Python practices

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-analysis-api.git
cd stock-analysis-api
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r backend/requirements.txt
```

4. Set up environment variables:
```bash
cp backend/.env.example backend/.env
# Edit .env and add your OpenAI API key
```

5. Run the application:
```bash
cd backend
uvicorn app.main:app --reload
```

The API will be available at:
- API Endpoint: `http://localhost:8000`
- Interactive Docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📚 API Documentation

### Endpoints

#### Stock Analysis
```http
POST /api/v1/stocks/analysis
```
Performs comprehensive stock analysis with AI insights.

Request body:
```json
{
    "symbols": ["AAPL", "MSFT"]
}
```

#### Market Sentiment
```http
POST /api/v1/stocks/sentiment
```
Analyzes market sentiment using AI agents.

Request body:
```json
{
    "symbols": ["AAPL", "TSLA"]
}
```

#### Get Plot
```http
GET /api/v1/stocks/plot/{filename}
```
Retrieves generated stock visualizations.

## 🛠️ Development

### Project Structure
```
backend/
├── app/
│   ├── agents/          # AutoGen agents
│   ├── api/             # API routes
│   ├── models/          # Pydantic models
│   ├── services/        # Business logic
│   ├── utils/           # Utility functions
│   ├── config.py        # Configuration
│   └── main.py         # Application entry
├── static/             # Static files
├── tests/             # Test suite
├── .env               # Environment variables
└── requirements.txt   # Dependencies
```

### Running Tests
```bash
pytest
```

### Code Quality
```bash
# Format code
black .

# Check types
mypy .

# Lint code
flake8
```

## 📊 Example Usage

```python
import httpx
import asyncio

async def analyze_stocks():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'http://localhost:8000/api/v1/stocks/analysis',
            json={'symbols': ['AAPL', 'MSFT']}
        )
        return response.json()

# Run analysis
result = asyncio.run(analyze_stocks())
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [AutoGen](https://microsoft.github.io/autogen/) for AI agent capabilities
- [yfinance](https://github.com/ranaroussi/yfinance) for stock data
- OpenAI for AI capabilities

## 📧 Contact

Aman - [@LinkedIN](https://www.linkedin.com/in/aman-soni-6b17b6223/) - aman1024soni@gmail.com
