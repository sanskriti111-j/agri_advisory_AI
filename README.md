# agri_advisory_AI
agri_advisory_AI  is a locally executed, AI-powered farm advisory system built entirely in Python using Visual Studio Code. It uses a modular multi-agent framework to simulate expert agricultural decision-making without requiring internet or cloud infrastructure.
All development and testing were done in VS Code, with CSV files as input, Python scripts for agent logic, and Ollama-powered LLaVA for image-based plant disease detection. The system includes a terminal-based advisory runner (run.py) and an optional Streamlit app (app.py) for a simple web interface.

The project integrates:

A Farmer Advisor that suggests suitable crops based on soil, water, and fertilizer inputs

A Market Researcher that analyzes demand, pricing, and trends from market-level CSVs

A Yield Predictor that estimates expected crop yield

A Vision-based Disease Detector using Ollama + LLaVA for leaf image diagnosis

All agents are orchestrated in a controller and executed from the terminal or UI

No cloud services were used. All logic and models run locally, making the system accessible and replicable in low-resource rural environments.

✅ Built With

Visual Studio Code (development environment)

Python 3 (core logic, data processing)

Streamlit (optional UI)

Ollama + LLaVA (on-device LLM + vision model)

CSV files (input data)

Here's a breakdown of how the system works:

1️⃣ Step 1: Input Farm ID

The user enters a Farm_ID (like F001) in the terminal or Streamlit app.

This Farm_ID is used to fetch all the relevant farm-level data from a CSV file (farmer_advisor_dataset.csv), such as:

Soil type (Loamy, Sandy, Clay)

Water availability (High, Medium, Low)

Fertilizer used (Organic, None, Synthetic)

Crop grown last season

This makes the system dynamic and personalized for each farm.

2️⃣ Step 2: Load Market Data

The system also loads a separate market-level CSV (market_researcher_dataset.csv) that contains:

Products (e.g., Wheat, Rice, Corn)

Demand Index, Market Price, Competitor Price

Seasonal and Economic indicators

This helps the Market Researcher agent assess which crops are profitable and in demand.

3️⃣ Step 3: Agent Collaboration (Modular Logic)

Each agent performs a specific role independently:

👨‍🌾 Farmer Advisor
Analyzes soil, water, and fertilizer conditions to recommend crops that are agronomically suitable.

📈 Market Researcher
Calculates demand trends, pricing, and competitiveness. It highlights which crops are most profitable.

🌾 Yield Predictor
Estimates the potential yield (in tons per acre) based on farm inputs like soil quality and water availability.

🖼️ (Optional) Disease Detector
If provided with a plant image, the system uses Ollama + LLaVA to analyze the image and describe visible symptoms or diseases.

All of these agents are modular — they run independently and return their conclusions to the main controller.

4️⃣ Step 4: Final Advisory Summary

The controller agent aggregates the results from all agents and builds a final advisory message. It includes:

Recommended crops

Predicted yield

Market demand and pricing overview

Past crop usage for context
