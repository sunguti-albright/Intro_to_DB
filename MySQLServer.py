"""
Write a simple python script that creates the database alx_book_store in your MySQL server.
Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :
Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.
"""

import mysql.connector
from mysql.connector import Error


# DB Connection
try:
    connection = mysql.connector.connect(
        host="localhost", user="root", password="Travisasutsa01."
    )
    if connection.is_connected():
        cursor = connection.cursor()
        # create DB if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("DB created successfully !!")
except mysql.connector.Error:
    print("Error while connecting to mysql")
finally:
    # Close cursor and connection
    if "cursor" in locals() and cursor:
        cursor.close()
    if "connection" in locals() and connection.is_connected():
        connection.close()
    print("MYSQL CONNECTION CLOSED :)")
