from flask import Flask, render_template, request, redirect, g
import mysql.connector
import os 
import uuid
from dotenv import load_dotenv
load_dotenv()


# Adding MYSQL functions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "admin"),
            database=os.getenv("DB_NAME"),
            port = os.getenv("DB_PORT")
        )
        g.cursor = g.db.cursor(dictionary=True)
        create_db()
        create_contacts_table()
    return g.db, g.cursor

# Create DB in case it does not exists
def create_db():
    db, cursor = get_db()
    db_name = os.getenv('DB_NAME', 'contacts_app2')
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.execute(f"USE {db_name}")
    db.commit()
    print(f"Database {db_name} created successfully")
    
# Create table in case it does not exists
def create_contacts_table():
    db, cursor = get_db()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS contacts ("
        "number INT AUTO_INCREMENT PRIMARY KEY,"
        "name VARCHAR(255) NOT NULL,"
        "phone VARCHAR(255),"
        "email VARCHAR(255) NOT NULL,"
        "gender VARCHAR(10),"
        "photo VARCHAR(255))")
    db.commit()
    print("Table created successfully")

def teardown_db(exception):
    db = g.pop('db', None)
    cursor = g.pop('cursor', None)
    if cursor is not None:
        cursor.close()
    if db is not None:
        db.close()

def get_contacts():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM contacts")
    result = cursor.fetchall()
    return result

def findByNumber(number):
    db, cursor = get_db()
    cursor.execute("SELECT * FROM contacts WHERE number = %s", (number,))
    result = cursor.fetchone()
    return result

def contact_exists(fullname, email):
    db, cursor = get_db()
    cursor.execute("SELECT * FROM contacts WHERE name = %s OR email = %s", (fullname, email))
    result = cursor.fetchone()
    return bool(result)

def search_contacts(search_name):
    db, cursor = get_db()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", ('%' + search_name + '%',))
    result = cursor.fetchall()
    return result

def create_contact(name, phone, email, gender, photo):
    db, cursor = get_db()
    cursor.execute(
        "INSERT INTO contacts (name, phone, email, gender, photo) VALUES (%s, %s, %s, %s, %s)",
        (name, phone, email, gender, photo))
    db.commit()
    return f"Contact {name} was added successfully"

def delete_contact(number):
    db, cursor = get_db()
    cursor.execute("DELETE FROM contacts WHERE number = %s", (number,))
    db.commit()
    return f"Contact {number} deleted successfully"

def update_contact(number, name, phone, email, gender):
   db, cursor = get_db()
   cursor.execute(
       "UPDATE contacts SET name = %s, phone = %s, email = %s, gender = %s WHERE number = %s",
       (name, phone, email, gender, number))
   db.commit()
