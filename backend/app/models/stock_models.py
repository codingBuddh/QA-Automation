from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime

class StockRequest(BaseModel):
    symbols: List[str] = Field(..., description="List of stock symbols to analyze")

class AgentResponse(BaseModel):
    content: Optional[str] = None
    role: Optional[str] = None
    type: Optional[str] = None
    metadata: Optional[Dict] = None

class AIAnalysis(BaseModel):
    chat_result: Optional[List[AgentResponse]] = Field(None, description="Results from the AI analysis")
    error: Optional[str] = Field(None, description="Error message if AI analysis failed")
    timestamp: datetime = Field(..., description="Time of analysis")

class StockAnalysisResponse(BaseModel):
    ytd_returns: Dict[str, float] = Field(..., description="YTD returns for each stock")
    plot_path: str = Field(..., description="Path to the generated plot")
    last_updated: datetime = Field(..., description="Timestamp of the analysis")
    ai_analysis: Optional[AIAnalysis] = Field(None, description="AI-powered analysis results")

class MarketSentiment(BaseModel):
    sentiment_analysis: Optional[Dict[str, Any]] = Field(None, description="Sentiment analysis results")
    error: Optional[str] = Field(None, description="Error message if analysis failed")
    timestamp: datetime = Field(..., description="Time of analysis") 