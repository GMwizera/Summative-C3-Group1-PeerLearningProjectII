from db import connect_db

def search_places():
    conn = connect_db()
    cursor = conn.cursor()
    
    category = input("Enter category (e.g., Restaurant, Concert, Conference): ").strip()
    price_range = input("Enter max price: ").strip()
    rating = input("Enter minimum rating (0-5): ").strip()
    
    query = """
    SELECT name, category, price, rating, available_seats 
    FROM venues 
    WHERE category=%s AND price<=%s AND rating>=%s
    """
    
    cursor.execute(query, (category, price_range, rating))
    results = cursor.fetchall()
    
    if results:
        print("\nAvailable Places:")
        for row in results:
            print(f"{row[0]} | {row[1]} | ${row[2]} | Rating: {row[3]} | Seats: {row[4]}")
    else:
        print("No matching places found.")
    
    conn.close()

if __name__ == "__main__":
    search_places()

