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
```



## Clone the repo
git clone https://github.com/itsabdullah15/ai-trip-planner.git
cd ai-trip-planner

## Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt



## 🔑 Setup Environment Variables

Create a .env file in the root directory and add your API keys:

GROQ_API_KEY=""
GOOGLE_MAPS_API_KEY=""
GPLACES_API_KEY=""
FOURSQUARE_API_KEY=""
TAVILA_API_KEY=""
OPENWEATHER_API_KEY=""
EXCHANGERATE_API_KEY=""


## 🛠️ Usage
Run the Agent Workflow
uvicorn main:app --reload --port 8000 

Run the Streamlit App
streamlit run streamlit_app.py

Then open 👉 http://localhost:8501 in your browser.


## 🧩 How It Works
	1.	GraphBuilder (agentic_workflow.py)
	•	Loads an LLM model (default: groq).
	•	Binds tools (weather, place search, calculator, currency).
	•	Builds a LangGraph agentic workflow with conditional tool invocation.
	2.	Tools
	•	Each tool wraps a specific function (API calls, calculations, etc.).
	•	Tools are dynamically invoked based on user query.
	3.	Execution Flow
    •   User → Agent → Tool (if needed) → Agent → Response


## 📌 Example Queries
	•	“What will the weather be in Paris next weekend?”
	•	“Find me the top 5 tourist attractions in Tokyo.”
	•	“Convert 500 USD to EUR.”
	•	“Calculate total expense for flights (400), hotel (300), and food (200).”

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

⸻
