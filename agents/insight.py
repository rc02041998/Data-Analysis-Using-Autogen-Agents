from autogen import AssistantAgent
from config import llm_config

InsightAgent = AssistantAgent(
    name="insight",
    llm_config=llm_config,
    system_message=(
        "You are an insight generator. Based on the analysis and charts, write clear and concise business insights and recommendations."
    )
)