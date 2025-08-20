# 🌤 Weather ETL Project

An end-to-end **Data Engineering pipeline** built with Python.  
The project **extracts real-time weather data** from APIs, **transforms** it into structured tables, **loads** it into both CSV and SQLite for storage, and provides **interactive dashboards** and **visualizations** for insights.  

---

## 🔹 Features
- **ETL Workflow**
  - Extracts live weather data for multiple cities
  - Transforms JSON response into clean tabular format
  - Loads data into:
    - CSV file (`weather_data.csv`)  
    - SQLite database (`weather.db`)  

- **Automation**
  - Runs hourly using Python’s `schedule` library  

- **Visualization**
  - 📊 Static plots with Matplotlib (`visualization.py`)  
  - 🌍 Interactive dashboard powered by Streamlit (`dashboard.py`)  

- **Database-Backed Dashboard**
  - Dashboard now queries **SQLite directly** (instead of CSV)  
  - Displays city-wise weather trends  
  - Includes a raw table view of the latest records  

---

## 🔹 Tech Stack
- **Python** (ETL + scripting)  
- **SQLite** (structured storage)  
- **Pandas** (data processing)  
- **Matplotlib** (static plots)  
- **Streamlit** (interactive dashboard)  
- **Schedule** (pipeline automation)  

---
weather_etl_project/
│
├── etl/
│ ├── extract.py # Extracts weather data from API
│ ├── transform.py # Cleans & structures the raw data
│ ├── load.py # Saves data to CSV & SQLite
│
├── config.py # API key & city list
├── main.py # Orchestrates ETL with scheduling
├── visualization.py # Generates static trend plots
├── dashboard.py # Interactive Streamlit dashboard
│
├── data/
│ ├── weather_data.csv # Historical data (CSV format)
│ ├── weather.db # SQLite database (structured storage)
│ └── *.png # Saved plots
│
├── requirements.txt # Python dependencies
└── README.md

## 🔹 Repository Structure
