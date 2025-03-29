from db import connect_db

def view_bookings(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT venues.name, reservations.seats, reservations.reservation_date 
    FROM reservations 
    JOIN venues ON reservations.venue_id = venues.venue_id
    WHERE reservations.user_id = %s
    """, (user_id,))
    
    results = cursor.fetchall()
    
    if results:
        print("\nYour Bookings:")
        for row in results:
            print(f"Venue: {row[0]}, Seats: {row[1]}, Date: {row[2]}")
    else:
        print("No reservations found.")
    
    conn.close()

if __name__ == "__main__":
    user_id = input("Enter your User ID: ").strip()
    view_bookings(user_id)

