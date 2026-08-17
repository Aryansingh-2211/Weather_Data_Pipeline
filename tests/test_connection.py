from db_connection import get_connection

conn = get_connection()

print("Connected Successfully")

conn.close()