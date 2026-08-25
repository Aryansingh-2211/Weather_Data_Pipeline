from db_connection import get_connection

conn = get_connection()

print("Connected Successfully")

conn.close()


# Data quality checks.........

df.isnull().sum()      # NULL CHECK

df.duplicated().sum()      #DUPLICATE CHECK

df["avg_temperature"].between(-10, 60).all()           #TEMPERATURE VALIDATION


df["avg_humidity"].between(0, 100).all()         #HUMIDITY VALIDATION