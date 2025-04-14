from typing import Any, Optional
from pydantic import BaseModel

class CampaignState(BaseModel):
    goal: str
    vector_db: Any
    sales_data: Any
    industry_data: Optional[Any] = None  # Added field for industry-specific data
    selected_domain: str = "automotives"  # Default domain
    selected_llm: str = "gemini"  # Default LLM
    market_analysis: Optional[str] = None
    audience_segments: Optional[str] = None
    campaign_strategy: Optional[str] = None
    campaign_content: Optional[str] = None
    simulation_results: Optional[str] = None
    final_report: Optional[str] = None
    email_status: Optional[str] = None