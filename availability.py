import mysql.connector
from db import connect_db

def check_availability():
    conn = connect_db()
    cursor = conn.cursor()

    venue_id = input("Enter Venue ID to check availability: ").strip()

    cursor.execute("SELECT available_seats FROM venues WHERE id = %s", (venue_id,))
    result = cursor.fetchone()

    if result:
        print(f"✅ Available Seats: {result[0]}")
    else:
        print("❌ Venue not found!")

    cursor.close()
    conn.close()

