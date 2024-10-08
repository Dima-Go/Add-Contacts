from flask import Flask, render_template, request, redirect
app = Flask(__name__)

rownumber = 1

contacts_list = [
    {
    'number': 1,
	'name': 'Arja Stark',
	'phone': '052-1111111',
	'email': 'arja@email.com',
	'photo': 'https://static.hbo.com/content/dam/hbodata/series/game-of-thrones/character/s5/arya-stark-1920.jpg'
    },
    {
    'number': 2,
    'name': 'Jon Snow',
	'phone': '052-2222222',
	'email': 'jon@email.com',
	'photo': 'https://static0.gamerantimages.com/wordpress/wp-content/uploads/2022/06/game-of-thrones-jon-snow.jpg'
    },
    {
	'number': 3,
    'name': 'Tyrion Lannister',
	'phone': '052-3333333',
	'email': 'tyrion@email.com',
	'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRug0gPA8aPfrdKbShyDYj0o61bYCla_43Tgg&s'
    }
]

rownumber = len(contacts_list) + 1

@app.route('/form')
def form():
    return render_template ("Form.html")

@app.route('/addContact', methods=['POST', 'GET'])
def addContact():
    global rownumber
    error = None
    fullname = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    gender = request.form['gender']
    if contact_exists(email, fullname):
        error = "Contact with this name or email already exists."
        return render_template("Form.html", error=error)
    new_contact = {
                   'number': rownumber, 
                   'name': fullname, 
                   'email': email, 
                   'phone': phone, 
                   'gender': gender
                   }
    contacts_list.append(new_contact)
    rownumber += 1
    return render_template ("Contacts.html", contacts=contacts_list)

@app.route('/contacts')
def contacts():
    return render_template ("Contacts.html", contacts=contacts_list)

def findByNumber(number):
			for contact in contacts_list:
				if contact['number'] == number:
					return contact
			return None

@app.route('/deleteContact/<int:number>')
def deleteContact(number):
    contact = findByNumber(number)
    if contact:
        contacts_list.remove(contact)
    return redirect('/contacts')

@app.route('/search', methods=['POST'])
def search():
	search = request.form['search_name']
	filtered_contacts = []
	for contact in contacts_list:
		if search.lower() in contact['name'].lower():
			filtered_contacts.append(contact)
	return render_template('Contacts.html', contacts = filtered_contacts)

def contact_exists(email, name):
    for contact in contacts_list:
        if contact['email'] == email or contact['name'] == name:
            return True
    return False

@app.route('/checkContact', methods=['GET'])
def check_contact():
    email = request.args.get('email')
    name = request.args.get('name')
    exists = contact_exists(email, name)
    return {'exists': exists}


if __name__ == "__main__": 
    app.run(port=5000, debug=True)