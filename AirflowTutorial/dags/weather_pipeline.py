from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

PROJECT_DIR = "/opt/airflow/weather-data-pipeline"

with DAG(
    dag_id="weather_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["Weather Pipeline", "Data Engineering"],
) as dag:

    # 1. Fetch Weather API data
    fetch_weather = BashOperator(
        task_id="fetch_weather",
        cwd=PROJECT_DIR,
        bash_command="python api/fetch_weather.py",
    )

    # 2. Bronze → Silver
    transform_silver = BashOperator(
        task_id="transform_silver",
        cwd=PROJECT_DIR,
        bash_command="python transform/silver_weather.py",
    )

    # 3. Silver → Gold
    transform_gold_daily = BashOperator(
        task_id="transform_gold_daily",
        cwd=PROJECT_DIR,
        bash_command="python transform/gold_daily_summary.py",
    )

    transform_gold_city = BashOperator(
        task_id="transform_gold_city",
        cwd=PROJECT_DIR,
        bash_command="python transform/gold_city_summary.py",
    )

    transform_gold_weather = BashOperator(
        task_id="transform_gold_weather",
        cwd=PROJECT_DIR,
        bash_command="python transform/gold_weather_summary.py",
    )

    # 4. Gold → SQL Server
    load_city_summary = BashOperator(
        task_id="load_city_summary",
        cwd=PROJECT_DIR,
        bash_command="python load/load_city_summary.py",
    )

    load_daily_summary = BashOperator(
        task_id="load_daily_summary",
        cwd=PROJECT_DIR,
        bash_command="python load/load_daily_summary1.py",
    )

    load_weather_summary = BashOperator(
        task_id="load_weather_summary",
        cwd=PROJECT_DIR,
        bash_command="python load/load_weather_summary.py",
    )

    # Pipeline dependencies

    fetch_weather >> transform_silver

    transform_silver >> transform_gold_daily
    transform_silver >> transform_gold_city
    transform_silver >> transform_gold_weather

    transform_gold_daily >> load_daily_summary
    transform_gold_city >> load_city_summary
    transform_gold_weather >> load_weather_summary