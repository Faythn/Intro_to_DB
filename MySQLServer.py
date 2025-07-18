import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',        # Replace with your MySQL username
            password='your_password'     # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print("An error occurred while connecting or creating the database:")
        print(e)

    finally:
        # Close the cursor and connection safely
        try:
            if cursor:
                cursor.close()
        except NameError:
            pass

        try:
            if connection and connection.is_connected():
                connection.close()
        except NameError:
            pass

if __name__ == "__main__":
    create_database()


