import mysql.connector  # Import MySQL connector to interact with the database
from db import connect_db  # Import function to establish a database connection

def search_places():
    """
    Function to search for places based on category, price, and rating.
    It connects to the database, retrieves matching venues, and displays them.
    """
    conn = connect_db()  # Establish database connection
    cursor = conn.cursor()  # Create a cursor object to execute SQL queries

    # Define the available categories
    categories = ['Restaurant', 'Concert', 'Conference', 'Park']

    # Display available categories to the user
    print("Available categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")  # Print categories with numbering

    # Get user input for category selection
    category_choice = input("Select a category by number: ")

    # Validate the user's category choice
    if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
        print("Invalid choice. Please choose a valid category.")
        return  # Exit function if input is invalid

    # Get the selected category based on user input
    selected_category = categories[int(category_choice) - 1]

    # Ask the user for additional search criteria
    max_price = input("Enter max price: ")  # Get maximum price limit from user
    minimum_rating = input("Enter minimum rating (0-5): ")  # Get minimum rating from user

    try:
        # Execute SQL query to search for matching venues in the database
        cursor.execute("""
            SELECT * FROM venues
            WHERE category = %s AND price <= %s AND rating >= %s
        """, (selected_category, max_price, minimum_rating))

        results = cursor.fetchall()  # Fetch all matching records

        # Display search results
        if results:
            print(f"Found {len(results)} matching places:")
            for result in results:
                print(f"Name: {result[1]}, Category: {result[2]}, Price: {result[3]}, Rating: {result[4]}")
        else:
            print("No matching places found.")  # No results found message

    except Exception as e:
        print(f"Error: {e}")  # Print error message if query execution fails

    conn.close()  # Close the database connection

# Run the function if the script is executed directly
if __name__ == "__main__":
    search_places()

