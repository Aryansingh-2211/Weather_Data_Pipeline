import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=host.docker.internal,1433;"
        "DATABASE=WeatherPipeline;"
        "UID=weather_user;"
        "PWD=Weather@123;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return conn