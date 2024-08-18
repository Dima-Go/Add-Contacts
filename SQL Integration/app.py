from flask import Flask, render_template, request, redirect, g
import mysql.connector
import os 
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/form')
def form():
    return render_template ("Form.html")

# Adding MYSQL functions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            port="3306",
            database="contacts_app2"
        )
        g.cursor = g.db.cursor(dictionary=True)
    return g.db, g.cursor

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

def create_contact(name, phone, email, gender):
    db, cursor = get_db()
    cursor.execute(
        "INSERT INTO contacts (name, phone, email, gender) VALUES (%s, %s, %s, %s)",
        (name, phone, email, gender)
    )
    db.commit()
    return "Contact was added successfully"

def delete_contact(number):
    db, cursor = get_db()
    cursor.execute("DELETE FROM contacts WHERE number = %s", (number,))
    db.commit()
    return "Contact was deleted successfully"

@app.route('/contacts')
def viewContacts():
   return render_template('Contacts.html', contacts=get_contacts())

@app.route('/addContact', methods=['POST', 'GET'])
def createContact():
    fullname = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']
    # photo = request.files['photo']
    
    # if 'photo' in request.files:
    #     photo = request.files['photo']
    #     if photo and photo.filename != '':
    #         file_path = os.path.join('Assignment/static/images', fullname + '.jpg')
    #         photo.save(file_path)
    #         photo_url = f'/static/images/{fullname}.jpg'
    #     else:
    #         photo_url = None
    # else:
    #     photo_url = None

    if not contact_exists(fullname, email):
        if not contact_exists(fullname, email):
            create_contact(fullname, phone, email, gender)
        return redirect('/contacts')
    else:
        return render_template('Contacts.html', message='Contact already exists')

    return redirect('/contacts')

@app.route('/deleteContact/<int:number>')
def deleteContact(number):
   delete_contact(number)
   return redirect('/contacts')

@app.route('/search', methods=['POST'])
def search():
   search_name = request.form['search_name']
   search_results = search_contacts(search_name)
   return render_template('Contacts.html', contacts=search_results)

if __name__ == "__main__": 
    app.run(port=5000, debug=True)
