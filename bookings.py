import mysql.connector

def view_my_bookings(username):
    cursor = None
    conn = None
    try:
        # Initialize database connection
        conn = mysql.connector.connect(
            host="localhost",         # Ensure this is correct
            user="root",     # Replace with your MySQL username
            password="", # Replace with your MySQL password
            database="summative"  # Replace with your database name
        )
        
        cursor = conn.cursor()
        print("Connection successful!")

        # Select user_id based on the username
        cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        user_id = cursor.fetchone()

        if user_id:
            user_id = user_id[0]
            print(f"Logged in as user ID: {user_id}")

            # Now fetch reservations for the user
            cursor.execute("SELECT * FROM reservations WHERE user_id = %s", (user_id,))
            reservations = cursor.fetchall()

            if reservations:
                print("Your bookings:")
                for reservation in reservations:
                    print(f"Reservation ID: {reservation[0]}, Venue ID: {reservation[1]}, Seats: {reservation[2]}, Date: {reservation[3]}")
            else:
                print("No bookings found.")
        else:
            print("User not found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close cursor and connection if they were initialized
        if cursor:
            cursor.close()
        if conn:
            conn.close()

