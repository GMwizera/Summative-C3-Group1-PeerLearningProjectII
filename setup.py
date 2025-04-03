import mysql.connector

# Database connection details
DB_HOST = "localhost"
DB_USER = "root"  # Change this if needed
DB_PASSWORD = ""  # Change this if needed
DB_NAME = "summative"

try:
    # Connect to MySQL Server
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    # Create Database if it does not exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"✅ Database '{DB_NAME}' has been created successfully!")

    # Connect to the new database
    conn.database = DB_NAME

    # Create Tables
    tables = {
        "users": """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """,
        "venues": """
            CREATE TABLE IF NOT EXISTS venues (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category VARCHAR(50),
                price DECIMAL(10,2),
                rating DECIMAL(2,1)
            )
        """,
        "reservations": """
            CREATE TABLE IF NOT EXISTS reservations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                venue_id INT,
                seats_reserved INT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (venue_id) REFERENCES venues(id) ON DELETE CASCADE
            )
        """
    }

    for table_name, table_query in tables.items():
        cursor.execute(table_query)
        print(f"✅ Table '{table_name}' created successfully!")

    # Insert Default Data (Only if tables are empty)
    cursor.execute("SELECT COUNT(*) FROM venues")
    if cursor.fetchone()[0] == 0:
        default_data = [
            (1, 'KCC', 'Conference', 100.00, 4.5),
            (2, 'BK Arena', 'Concert', 50.00, 4.7),
            (3, 'Marriott', 'Restaurant', 30.00, 4.3),
            (4, 'Serena', 'Park', 20.00, 4.6)
        ]
        cursor.executemany("INSERT INTO venues (id, name, category, price, rating) VALUES (%s, %s, %s, %s, %s)", default_data)
        conn.commit()
        print("✅ Default data inserted successfully!")

    # Close Connection
    cursor.close()
    conn.close()
    print("🎉 Setup completed successfully!")

except mysql.connector.Error as err:
    if "Access denied" in str(err):
        print("❌ Access Denied: Please make sure you are logged in as root.")
        print("💡 Try running: sudo python3 setup.py")
    elif "Unknown database" in str(err):
        print(f"⚠️ Database '{DB_NAME}' not found. Creating it now...")
    elif "Can't connect" in str(err):
        print("❌ Error: Unable to connect to MySQL. Make sure MySQL is running!")
    else:
        print(f"⚠️ Unexpected Error: {err}")

