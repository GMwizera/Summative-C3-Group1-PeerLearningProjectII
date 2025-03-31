import mysql.connector
from db import connect_db

def search_places():
    conn = connect_db()
    cursor = conn.cursor()

    # Define the available categories
    categories = ['Restaurant', 'Concert', 'Conference', 'Park']

    # Provide the user with options to choose a category
    print("Available categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    category_choice = input("Select a category by number: ")

    # Validate the choice
    if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
        print("Invalid choice. Please choose a valid category.")
        return

    selected_category = categories[int(category_choice) - 1]

    # Ask for additional search parameters
    max_price = input("Enter max price: ")
    minimum_rating = input("Enter minimum rating (0-5): ")

    try:
        # Execute the query with the selected category, max price, and rating
        cursor.execute("""
            SELECT * FROM venues
            WHERE category = %s AND price <= %s AND rating >= %s
        """, (selected_category, max_price, minimum_rating))

        results = cursor.fetchall()

        # Show the results
        if results:
            print(f"Found {len(results)} matching places:")
            for result in results:
                print(f"Name: {result[1]}, Category: {result[2]}, Price: {result[3]}, Rating: {result[4]}")
        else:
            print("No matching places found.")
    except Exception as e:
        print(f"Error: {e}")

    conn.close()

if __name__ == "__main__":
    search_places()

