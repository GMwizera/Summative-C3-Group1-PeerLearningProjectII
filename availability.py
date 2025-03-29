from db import connect_db

def check_availability():
    conn = connect_db()
    cursor = conn.cursor()
    
    venue_id = input("Enter Venue ID to check availability: ").strip()
    
    cursor.execute("SELECT available_seats FROM venues WHERE venue_id = %s", (venue_id,))
    result = cursor.fetchone()
    
    if result and result[0] > 0:
        print(f"Seats available: {result[0]}")
    else:
        print("Sorry, this venue is fully booked.")
    
    conn.close()

if __name__ == "__main__":
    check_availability()

