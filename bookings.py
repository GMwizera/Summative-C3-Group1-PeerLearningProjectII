import mysql.connector
from db import connect_db

def view_my_bookings(username):
    conn = connect_db()
    cursor = conn.cursor()

    # Fetch user_id from username
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]

        # Fetch reservations with venue name
        cursor.execute("""
            SELECT venues.name, reservations.seats_reserved
            FROM reservations
            JOIN venues ON reservations.venue_id = venues.venue_id
            WHERE reservations.user_id = %s
        """, (user_id,))

        bookings = cursor.fetchall()

        if bookings:
            print("\nYour Reservations:")
            for venue_name, seats_reserved in bookings:
                print(f"- {venue_name}: {seats_reserved} seat(s) reserved")
        else:
            print("No reservations found.")
    else:
        print("User not found. Please register first.")

    conn.close()

if _name_ == "_main_":
    username = input("Enter your username: ")
    view_my_bookings(username)
