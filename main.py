try:
    import mysql.connector
    from login import login, register
    from search import search_places
    from availability import check_availability
    from reservation import make_reservation
    from bookings import view_my_bookings
except ModuleNotFoundError as e:
    missing_module = str(e).split("'")[1]
    print(f"Error: Missing dependency '{missing_module}'.")
    print("To install all required dependencies, run:")
    print("    ./setup.sh")
    exit(1)

def main():
    print("\nWelcome to the My Guide And Reservation App!")
    
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            user = login()
            if user:
                break  # Proceed to the main menu
        elif choice == '2':
            register()  # Call the register function
            print("✅ Registration successful! Please log in.")
        elif choice == '3':
            print("Goodbye!")
            exit()
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

    # Main menu after successful login
    while True:
        print("\nMenu:")
        print("1. Search for Places")
        print("2. Check Availability")
        print("3. Make a Reservation")
        print("4. View My Bookings")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            search_places()
        elif choice == '2':
            check_availability()
        elif choice == '3':
            make_reservation(user)
        elif choice == '4':
            view_my_bookings(user)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

