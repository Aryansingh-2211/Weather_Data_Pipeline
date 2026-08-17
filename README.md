# 🌦️ Weather Data Engineering Pipeline

An end-to-end data engineering pipeline that collects weather data from an API, processes the data through Bronze, Silver, and Gold layers, orchestrates the workflow using Apache Airflow, and loads analytical data into SQL Server.

## 🏗️ Architecture

```text
OpenWeather API
       ↓
Python API Extraction
       ↓
Bronze Layer - Raw JSON
       ↓
Silver Layer - Cleaned Data
       ↓
Gold Layer - Aggregated Data
       ↓
Apache Airflow
       ↓
SQL Server
       