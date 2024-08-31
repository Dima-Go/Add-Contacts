from flask import Flask, render_template, request, redirect, g
import mysql.connector
import os 
import uuid
from bson import ObjectId
from dotenv import load_dotenv
load_dotenv()

db_to_use = os.getenv("DATABASE_TYPE", "MONGO") # "MYSQL" or "MONGO"

if db_to_use == "MYSQL":
    from data_sql import (get_contacts, create_contact, get_db, create_db, create_contacts_table, teardown_db, findByNumber,contact_exists, search_contacts, delete_contact, update_contact)

elif db_to_use == "MONGO":
    from data_mongo import (get_contacts, create_contact, findByNumber,contact_exists, search_contacts, delete_contact, update_contact)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/'

@app.route('/form')
def form():
    return render_template ("Form.html")

@app.route('/contacts')
def viewContacts():
   return render_template('Contacts.html', contacts=get_contacts())

@app.route('/addContact', methods=['POST', 'GET'])
def createContact():
    fullname = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']
    photo = request.files['photo']
    
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo and photo.filename != '':
            photo_filename = str(uuid.uuid4()) + os.path.splitext(photo.filename)[1]
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], fullname + '.jpg')
            # photo.save(file_path)
            photo_url = f'/static/images/{fullname}.jpg'
        else:
            photo_url = None
    else:
        photo_url = None

    if not contact_exists(fullname, email):
        if not contact_exists(fullname, email):
            create_contact(fullname, phone, email, gender, f"{fullname}.jpg")
        return redirect('/contacts')
    else:
        # return redirect('/contacts', message='Contact already exists')
        return render_template('Contacts.html', message='Contact already exists')

@app.route('/deleteContact/<number>')
def deleteContact(number):
    if db_to_use == "MONGO":
        delete_contact(ObjectId(number))
    else:
        delete_contact(number)
    return redirect('/contacts')

@app.route('/editContact/<number>')
def editContact(number):
    if db_to_use == "MONGO":
        contact = findByNumber(ObjectId(number))
    else:
        contact = findByNumber(number)
    return render_template('editContactForm.html', contact=contact)

@app.route('/saveUpdatedContact/<number>', methods=['POST'])
def saveUpdatedContact(number):
   fullname = request.form['name']
   phone = request.form['phone']
   email = request.form['email']
   gender = request.form['gender']
   if db_to_use == "MONGO":
       update_contact(ObjectId(number), fullname, phone, email, gender)
   else:
       update_contact(number, fullname, phone, email, gender)
   return redirect('/contacts')

@app.route('/search', methods=['POST'])
def search():
   search_name = request.form['search_name']
   search_results = search_contacts(search_name)
   return render_template('Contacts.html', contacts=search_results)

if __name__ == "__main__": 
    # if db_to_use == "MYSQL":
    #     get_db()
    #     create_db()
    #     create_contacts_table()
    #     app.teardown_appcontext(teardown_db)
    app.run(port=5000, debug=True)
