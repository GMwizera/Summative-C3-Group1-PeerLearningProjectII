import mysql.connector
from db import connect_db

def insert_rwandan_venues():
    conn = connect_db()
    cursor = conn.cursor()

    venues = [
        # Conference Venues
        ('Conference', 'Kigali Convention Centre (KCC)', 100000, 5, 'Kigali'),
        ('Conference', 'Serena Hotel Kigali', 80000, 4.5, 'Kigali'),
        ('Conference', 'Marriott Kigali', 90000, 4.5, 'Kigali'),
        
        # Concert Venue
        ('Concert', 'BK Arena', 20000, 4, 'Kigali')
    ]

    try:
        cursor.executemany("""
            INSERT INTO venues (category, name, price, rating, location)
            VALUES (%s, %s, %s, %s, %s)
        """, venues)

        conn.commit()
        print("Rwandan venues inserted successfully!")

    except Exception as e:
        print(f"Error inserting venues: {e}")
    
    finally:
        conn.close()

if _name_ == "_main_":
    insert_rwandan_venues()
