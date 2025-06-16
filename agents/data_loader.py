from autogen import AssistantAgent
from config import llm_config

# Correct path relative to the execution context
file_path = "sales.csv"

DataLoaderAgent = AssistantAgent(
    name="data_loader",
    llm_config=llm_config,
    system_message=(
        f"You are a data loader. Your job is to read and explore the dataset '{file_path}'. "
        f"The dataset contains Date, Category, Region, Quantity columns as independent variables, "
        f"and Sales is the dependent variable. "
        "Provide summary statistics, handle missing values, and prepare the data for analysis. "
        "Use only valid Python syntax. Use 'from sklearn.impute import SimpleImputer' for imputing missing data."
    )
)