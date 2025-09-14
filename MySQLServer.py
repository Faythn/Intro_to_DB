import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (replace with your credentials)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',    # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print("An error occurred while connecting or creating the database:")
        print(e)

    finally:
        # Safely close cursor
        if cursor is not None:
            try:
                cursor.close()
            except mysql.connector.Error as e:
                print("Error closing cursor:", e)

        # Safely close connection
        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except mysql.connector.Error as e:
                print("Error closing connection:", e)

if __name__ == "__main__":
    create_database()
