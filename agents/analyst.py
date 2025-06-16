from autogen import AssistantAgent
from config import llm_config

AnalystAgent = AssistantAgent(
    name="analyst",
    llm_config=llm_config,
    system_message=(
        "You are a skilled data analyst. Your task is to analyze the pre-processed dataset received from the data loader. "
        "Identify key trends, correlations between variables (e.g., Quantity and Sales), seasonal patterns from the Date column, "
        "and detect any anomalies such as sudden drops or spikes in Sales. "
        "Summarize your findings clearly. Use pandas or numpy where needed. "
        "Strictly follow the above instructions and use valid Python syntax only."
    )
)