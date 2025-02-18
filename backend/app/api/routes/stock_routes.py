from fastapi import APIRouter, HTTPException, Response, status
from app.models.stock_models import StockRequest, StockAnalysisResponse, MarketSentiment
from app.services.stock_service import StockService
from app.config import settings
from typing import List
import os

router = APIRouter()

@router.post(
    "/analysis",
    response_model=StockAnalysisResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyze Stocks with AI",
    description="Performs comprehensive stock analysis combining traditional metrics with AI insights"
)
async def analyze_stocks(request: StockRequest):
    """
    Analyze stocks and generate visualization with AI insights.
    
    Parameters:
    - **symbols**: List of stock symbols to analyze (e.g., ["AAPL", "MSFT"])
    
    Returns:
    - **ytd_returns**: Year-to-date returns for each stock
    - **plot_path**: Path to the generated visualization
    - **last_updated**: Timestamp of the analysis
    - **ai_analysis**: AI-powered insights including:
        - Technical indicators
        - Market sentiment
        - Performance analysis
    
    Example:
    ```python
    {
        "symbols": ["AAPL", "MSFT"]
    }
    ```
    """
    try:
        result = await StockService.analyze_stocks(request.symbols)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/sentiment",
    response_model=MarketSentiment,
    status_code=status.HTTP_200_OK,
    summary="Get Market Sentiment",
    description="Analyzes market sentiment using AI for the specified stocks"
)
async def get_market_sentiment(request: StockRequest):
    """
    Get market sentiment analysis for the specified stocks.
    
    Parameters:
    - **symbols**: List of stock symbols to analyze sentiment for
    
    Returns:
    - **sentiment_analysis**: Detailed sentiment analysis including:
        - News sentiment
        - Social media trends
        - Analyst recommendations
    - **timestamp**: Time of analysis
    - **error**: Error message if analysis failed
    
    Example:
    ```python
    {
        "symbols": ["AAPL", "TSLA"]
    }
    ```
    """
    try:
        result = await StockService.get_market_sentiment(request.symbols)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/plot/{filename}",
    response_class=Response,
    status_code=status.HTTP_200_OK,
    summary="Get Stock Plot",
    description="Retrieves the generated stock price visualization"
)
async def get_plot(filename: str):
    """
    Get the generated plot image.
    
    Parameters:
    - **filename**: Name of the plot file to retrieve
    
    Returns:
    - PNG image of the stock price visualization
    
    Raises:
    - 404: If the plot file is not found
    
    Example:
    ```
    GET /api/v1/stocks/plot/stock_prices_YTD_20240218.png
    ```
    """
    file_path = settings.PLOT_FOLDER / filename
    if not file_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plot file '{filename}' not found"
        )
    
    with open(file_path, "rb") as f:
        image_data = f.read()
    
    return Response(
        content=image_data,
        media_type="image/png",
        headers={"Content-Disposition": f"inline; filename={filename}"}
    ) 