import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""  # If you set a password in Step 2, update it here.
DB_NAME = "summative"

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        if "Access denied" in str(err):
            print("❌ Access Denied: Check your MySQL user credentials.")
            print("💡 Try running: sudo mysql and updating authentication settings.")
        else:
            print(f"⚠️ Database Connection Error: {err}")
        return None

