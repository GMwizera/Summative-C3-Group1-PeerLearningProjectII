import mysql.connector
import getpass
import hashlib
from db import connect_db

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n📝 Register a New Account")
    username = input("Enter a username: ").strip()
    password = getpass.getpass("Enter a password: ")

    # Hash the password before storing it
    hashed_password = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        print("✅ Registration successful!")
    except mysql.connector.Error as err:
        print(f"⚠️ Error: {err}")
    finally:
        cursor.close()
        conn.close()
def login():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n🔐 Login to Your Account")
    username = input("Enter your username: ").strip()
    password = getpass.getpass("Enter your password: ")

    # Retrieve the stored hashed password for the given usernam
    cursor.execute("SELECT user_id, username, password FROM users WHERE username = %s", (username,))

    user = cursor.fetchone()

    if user:
        user_id, username, stored_hashed_password = user
        
        # Check if the entered password matches the stored hashed password
        if hash_password(password) == stored_hashed_password:
            print(f"✅ Login successful! Welcome, {username}.")
            return {"user_id": user_id, "username": username}  # Return user details
        else:
            print("❌ Incorrect password. Please try again.")
    else:
        print("❌ Username not found.")

    cursor.close()
    conn.close()
    return user  # Return None if login fails
if __name__ == "__main__":
    choice = input("Register (R) or Login (L)? ").strip().lower()
    if choice == 'r':
        register()
    elif choice == 'l':
        login()
    else:
        print("Invalid choice. Please enter 'R' for Register or 'L' for Login.")
