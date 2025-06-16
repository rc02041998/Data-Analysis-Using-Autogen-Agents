
# AutoGen Data Analysis Agent System

This project demonstrates an **autonomous multi-agent system** using [AutoGen](https://github.com/microsoft/autogen) to automate the **end-to-end process of data analysis** on a CSV file. Agents collaborate to load, clean, analyze, visualize, and summarize insights from structured data.

---

## Project Structure

```
AutoGen-Data-Analysis/
├── agents/
│   ├── analyst.py         # AnalystAgent: Finds trends, patterns, anomalies
│   ├── data_loader.py     # DataLoaderAgent: Loads & preprocesses the CSV data
│   ├── plotter.py         # PlotterAgent: Generates and saves plots
│   └── insight.py         # InsightAgent: Summarizes insights
├── config.py              # Loads LLM config list from OAI_CONFIG_LIST
├── main.py                # Starts the multi-agent data analysis workflow
├── data/
│   └── sales.csv          # Input CSV dataset (ignored in .gitignore)
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

---

##  How It Works

###  Agents Involved

| Agent         | Role                                                                 |
|---------------|----------------------------------------------------------------------|
| **UserProxy** | Initiates the task and supervises the conversation                  |
| **DataLoader**| Loads `sales.csv`, handles missing values, and prepares the data     |
| **Analyst**   | Performs statistical and trend analysis                              |
| **Plotter**   | Visualizes insights using `matplotlib` and `seaborn`                |
| **Insight**   | Generates human-readable summaries of the insights                   |

###  Workflow

1. `user_proxy` sends a task message:  
   _“Load and explore the './data/sales.csv' file. Then pass it to the analyst for analysis, the plotter for visualization, and the insight agent to summarize insights.”_

2. Agents collaborate in sequence:
   - **DataLoaderAgent** loads and cleans the dataset.
   - **AnalystAgent** finds trends and statistical patterns.
   - **PlotterAgent** generates plots and saves them in `data/`.
   - **InsightAgent** summarizes insights based on analysis.

---

##  Sample Input (`data/sales.csv`)

```csv
Date,Category,Region,Quantity,Sales
2024-01-01,Electronics,North,10,5000
2024-01-02,Furniture,South,5,2500
...
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rc02041998/Data-Analysis-Using-Autogen-Agents.git
cd Data-Analysis-Using-Autogen-Agents
```

### 2. Create and Activate Environment

```bash
python3 -m venv autogen_env
source autogen_env/bin/activate  # or use .\autogen_env\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install pandas matplotlib seaborn scikit-learn autogen
```

### 4. Set Up Your LLM Configuration

Create an `OAI_CONFIG_LIST` file (JSON) with model details:

```json
[
  {
    "model": "llama3.2",
    "api_type": "ollama",
    "base_url": "http://localhost:11434",
    "api_key": ""
  }
]
```

---

##  Run the Workflow

```bash
python main.py
```

You’ll see console outputs from each agent, including summaries and references to saved plots in the `data/` directory.

---

##  Output

- Summary statistics
- Cleaned dataset
- Time series and region-wise plots (saved as PNG)
- Text-based insight summary

---

##  Notes

- Plots are saved to `data/` (e.g., `data/sales_over_time.png`)
- The `sales.csv` file should be placed under the `data/` directory
- The project uses in-process code execution; no Docker required (can be toggled)

---

## Technologies Used

- **Python** 
- **AutoGen** by Microsoft
- **Ollama** or any LLM backend
- **Pandas, Seaborn, Matplotlib, Scikit-learn**

---


##  Contributing

PRs welcome! If you want to add:
- New agent types (e.g., ReportGenerator)
- Advanced analysis like forecasting
- Integration with LangChain/ChromaDB

Please submit an issue or open a pull request.

---

##  Contact

**Rohit Kumar**  
Email: rc02041998@gmail.com 
LinkedIn: https://www.linkedin.com/in/rohit-kumar-2b6736161/
