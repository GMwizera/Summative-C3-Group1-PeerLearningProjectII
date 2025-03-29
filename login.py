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
    
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                       (username, email, hashed_password))
        conn.commit()
        print("Registration successful!")
    except:
        print("User already exists.")
    
    conn.close()

def login():
    conn = connect_db()
    cursor = conn.cursor()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
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
    else:
        login()

