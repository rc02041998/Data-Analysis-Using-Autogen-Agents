import os
from autogen import ConversableAgent
from config import llm_config

# Ensure 'data/' directory exists
os.makedirs("data", exist_ok=True)

PlotterAgent = ConversableAgent(
    name="plotter",
    llm_config=llm_config,
    system_message=(
        "You are a plotting assistant. Generate and execute Python matplotlib/seaborn code "
        "to create plots based on the provided pandas DataFrame. "
        "Always save plots as PNGs in the 'data/' folder using `plt.savefig('data/filename.png')`, "
        "and then call `plt.close()` to release memory. "
        "Use descriptive and unique filenames like 'sales_over_time.png'. "
        "Do NOT use `plt.show()` under any circumstances."
    ),
    code_execution_config={
        "work_dir": "data",
        "use_docker": False
    }
)