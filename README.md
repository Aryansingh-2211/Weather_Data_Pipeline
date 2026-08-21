#  Weather Data Engineering Pipeline

An end-to-end data engineering pipeline that collects weather data from an API, processes the data through Bronze, Silver, and Gold layers, orchestrates the workflow using Apache Airflow, and loads analytical data into SQL Server.

##  Architecture

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
       
<<<<<<< Updated upstream
=======

##  Project Screenshots.....

###  Airflow Pipeline

The complete weather pipeline is orchestrated using Apache Airflow.

[Airflow Pipeline](screenshots/airflow_pipeline.png)

###  SQL Server

Gold analytical tables are loaded into SQL Server.

[SQL Server Results](screenshots/sql_server_result.png)
>>>>>>> Stashed changes
