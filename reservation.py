from db import connect_db

def make_reservation(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    venue_id = input("Enter Venue ID to reserve: ").strip()
    seats = int(input("Enter number of seats: "))
    
    cursor.execute("SELECT available_seats FROM venues WHERE venue_id = %s", (venue_id,))
    available = cursor.fetchone()
    
    if available and available[0] >= seats:
        cursor.execute("INSERT INTO reservations (user_id, venue_id, seats) VALUES (%s, %s, %s)", 
                       (user_id, venue_id, seats))
        cursor.execute("UPDATE venues SET available_seats = available_seats - %s WHERE venue_id = %s", 
                       (seats, venue_id))
        conn.commit()
        print("Reservation successful!")
    else:
        print("Not enough seats available.")
    
    conn.close()

if __name__ == "__main__":
    user_id = input("Enter your User ID: ").strip()  # Assume the user has logged in
    make_reservation(user_id)

