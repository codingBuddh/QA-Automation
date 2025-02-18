from datetime import datetime
from typing import List, Dict, Any
from app.utils.stock_utils import get_ytd_stock_data
from app.agents.stock_agents import code_executor_agent, code_writer_agent
from app.models.stock_models import AgentResponse, AIAnalysis, MarketSentiment

class StockService:
    @staticmethod
    def _format_chat_result(result: List[Dict[str, Any]]) -> List[AgentResponse]:
        """Format the chat result to match the AgentResponse model"""
        formatted_results = []
        for msg in result:
            formatted_results.append(AgentResponse(
                content=msg.get('content'),
                role=msg.get('role'),
                type=msg.get('type'),
                metadata=msg.get('metadata')
            ))
        return formatted_results

    @staticmethod
    async def analyze_stocks(symbols: List[str]) -> Dict:
        """
        Analyze stocks using both traditional analysis and AI agents
        """
        # Get basic stock analysis
        basic_analysis = get_ytd_stock_data(symbols)
        
        # Use agents for advanced analysis
        analysis_prompt = f"""
        Analyze the following stocks: {', '.join(symbols)}
        Current date: {datetime.now().date()}
        
        Tasks:
        1. Calculate and explain YTD Performance
        2. Generate key technical indicators (RSI, MACD, Moving Averages)
        3. Analyze market sentiment
        
        Requirements:
        - Put all code in markdown code blocks
        - Save any plots to files
        - Provide clear explanations
        - When finished, reply with 'TERMINATE'
        """
        
        try:
            # Initiate chat between agents with termination handling
            chat_result = code_executor_agent.initiate_chat(
                code_writer_agent,
                message=analysis_prompt,
                max_turns=10  # Limit conversation turns
            )
            
            # Format and add AI analysis to the response
            formatted_chat = StockService._format_chat_result(chat_result)
            basic_analysis['ai_analysis'] = AIAnalysis(
                chat_result=formatted_chat,
                timestamp=datetime.now()
            ).dict()
            
        except Exception as e:
            basic_analysis['ai_analysis'] = AIAnalysis(
                error=str(e),
                timestamp=datetime.now()
            ).dict()
        
        return basic_analysis

    @staticmethod
    async def get_market_sentiment(symbols: List[str]) -> Dict:
        """
        Get market sentiment analysis using AI agents
        """
        sentiment_prompt = f"""
        Analyze market sentiment for: {', '.join(symbols)}
        
        Tasks:
        1. Analyze recent news sentiment (last 7 days)
        2. Check social media trends
        3. Review analyst recommendations
        
        Requirements:
        - Provide sentiment scores (0-100)
        - Include source citations
        - When analysis is complete, reply with 'TERMINATE'
        """
        
        try:
            # Initiate chat with termination handling
            chat_result = code_executor_agent.initiate_chat(
                code_writer_agent,
                message=sentiment_prompt,
                max_turns=5  # Limit conversation turns for sentiment analysis
            )
            
            return MarketSentiment(
                sentiment_analysis={'messages': StockService._format_chat_result(chat_result)},
                timestamp=datetime.now()
            ).dict()
            
        except Exception as e:
            return MarketSentiment(
                error=str(e),
                timestamp=datetime.now()
            ).dict() 