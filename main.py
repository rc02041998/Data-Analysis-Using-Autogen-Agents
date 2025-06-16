from autogen import UserProxyAgent
from agents.data_loader import DataLoaderAgent
from agents.analyst import AnalystAgent
from agents.plotter import PlotterAgent
from agents.insight import InsightAgent

# User proxy with code execution
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "data", "use_docker": False}
)

# Orchestration Logic
def data_analysis_workflow():
    user_proxy.initiate_chat(
        DataLoaderAgent,
        message=(
            "Load and explore the 'sales.csv' file. "
            "Then pass it to the analyst for analysis, "
            "the plotter for visualization, "
            "and the insight agent to summarize insights."
        ),
        agents=[AnalystAgent, PlotterAgent, InsightAgent],
        max_turns=20,
        summary_method="reflection_with_llm"
    )

if __name__ == "__main__":
    data_analysis_workflow()
