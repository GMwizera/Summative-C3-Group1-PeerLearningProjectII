#this is the script that has the logic for allowing users to make a reservation at a venue
import mysql.connector
from db import connect_db

def make_reservation(username):
    conn = connect_db()
    cursor = conn.cursor()

    # Fetch user_id using the username
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]

        venue_id = input("Enter Venue ID to reserve: ")
        seats_reserved = input("Enter number of seats: ")  # Capture input here

        # Insert reservation using user_id
        cursor.execute("INSERT INTO reservations (user_id, venue_id, seats_reserved) VALUES (%s, %s, %s)",
                       (user_id, venue_id, seats_reserved))
        conn.commit()
        print("Reservation successful!")
    else:
        print("User not found. Please register first.")

    conn.close()

if __name__ == "__main__":
    username = input("Enter your username: ")
    make_reservation(username
