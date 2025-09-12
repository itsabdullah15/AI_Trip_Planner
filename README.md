# 🧳 AI Trip Planner

An **AI-powered travel assistant** that helps you plan trips using intelligent workflows.  
It integrates with weather APIs, place search services, calculators, and currency converters  
to provide an end-to-end trip planning experience.

---

## 🚀 Features

- 🌦️ **Weather Information** – Get real-time weather details for any location.  
- 📍 **Place Search** – Find tourist spots, hotels, restaurants, and more.  
- 💰 **Expense Calculator** – Estimate and manage travel expenses.  
- 💱 **Currency Conversion** – Convert expenses across currencies.  
- 🧠 **Agentic Workflow** – Uses LLM-powered agents + LangGraph to handle dynamic queries.  

---

## 🗂️ Project Structure

```text
AI_TRIP_PLANNER/
│── Al_Trip_Planner/
│   ├── agent/
│   │   └── agentic_workflow.py   # Defines the Agentic Workflow Graph
│   ├── tools/                    # Tools used by the agent
│   │   ├── weather_info_tool.py
│   │   ├── place_search_tool.py
│   │   ├── expense_calculator_tool.py
│   │   ├── currency_conversion_tool.py
│   │   └── calculator_tool.py
│   ├── config/                   # Configuration files
│   ├── exception/                # Custom exceptions
│   ├── logger/                   # Logging utilities
│   ├── notebook/                 # Jupyter notebooks for testing
│   ├── prompt_library/           # System & agent prompts
│   └── utils/                    # Helpers (e.g., ModelLoader)
│
├── app.py                        # FastAPI / Streamlit app entry point
├── streamlit_app.py              # Streamlit frontend
├── main.py                       # Script runner
├── requirements.txt              # Dependencies
├── setup.py                      # Setup file
├── pyproject.toml                # Project metadata
├── README.md                     # Project documentation