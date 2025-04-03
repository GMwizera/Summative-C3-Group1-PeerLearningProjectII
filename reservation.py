import mysql.connector
from datetime import date

def make_reservation(user):
    cursor = None
    conn = None
    try:
        # Check if 'user_id' exists in the user dictionary
        user_id = user.get("id") or user.get("user_id") 
        # Try both 'id' and 'user_id'
        if not user_id:
            print("❌ Error: User ID not found. Please log in again.")
            return
        print(f"Logged in as User ID: {user_id}")
       # Initialize database connection
        conn = mysql.connector.connect(
            host="localhost",         # Ensure this is correct
            user="root",     # Replace with your MySQL username
            password="", # Replace with your MySQL password
            database="summative"  # Replace with your database name
        )
        
        cursor = conn.cursor()
        print("Connection successful!")

        # Get Venue ID and Seats
        venue_id = input("Enter Venue ID to book: ")
        seats = input("Enter number of seats: ")

        # Validate input
        try:
            venue_id = int(venue_id)
            seats = int(seats)
        except ValueError:
            print("Please enter valid integer values for venue ID and number of seats.")
            return
        
        # Set the reservation date
        reservation_date = date.today()

        # Insert reservation into the database
        cursor.execute("""
            INSERT INTO reservations (user_id, venue_id, seats_reserved, date)
            VALUES (%s, %s, %s, %s)
        """, (user['user_id'], venue_id, seats, reservation_date))

        conn.commit()
        print("Reservation successful!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    finally:
        # Close cursor and connection if they were initialized
        if cursor:
            cursor.close()
        if conn:
            conn.close()

