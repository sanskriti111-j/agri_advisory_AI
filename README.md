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
