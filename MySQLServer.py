import mysql.connector
try: 
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Maryam@2112",
        port="3307"
    )
    my_cursor = my_db.cursor()
    my_cursor.execute("""CREATE DATABASE IF NOT EXISTS alx_book_store""")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"Error to create database {e}");
    