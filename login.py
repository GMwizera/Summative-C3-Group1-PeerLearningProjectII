import getpass
import hashlib
from db import connect_db

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    conn = connect_db()
    cursor = conn.cursor()
    
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    hashed_password = hash_password(password)
    
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        print("User already exists.")
        conn.close()
        return

    try:
        # Insert the new user into the users table
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, hashed_password))
        conn.commit()
        print("Registration successful!")
    except Exception as e:
        print("User already exists.")

    conn.close()


def login():
    """Handles the user login process."""
    conn = connect_db()
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    # Fetch the stored hashed password for the user
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    # Check if the user exists and the password matches
    if user and user[0] == hash_password(password):
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None

if __name__ == "__main__":
    choice = input("Register (R) or Login (L)? ").strip().lower()
    if choice == 'r':
        register()
    elif choice == 'l':
        login()
    else:
        print("Invalid choice. Please enter 'R' for Register or 'L' for Login.")
