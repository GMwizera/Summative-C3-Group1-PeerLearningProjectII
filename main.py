from login import login
from search import search_places
from availability import check_availability
from reservation import make_reservation
from bookings import view_bookings

def main():
    user = login()
    if user:
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
                view_bookings(user)
            elif choice == '5':
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()

