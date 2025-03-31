import mysql.connector  # Import MySQL connector module for database interaction

def connect_db():
    """
    Establishes a connection to the MySQL database.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection object to interact with the database.
    """
    return mysql.connector.connect(
        host="localhost",  # Database server hostname
        user="root",       # Database username
        password="123",    # Database password (Consider using environment variables for security)
        database="summative"  # Target database name
    )
