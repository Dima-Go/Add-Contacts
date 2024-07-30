from flask import Flask, render_template, request
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




# @app.route("/welcome")
# def welcome(): 
#     return ("<h1>Hello World!</h1>")


# @app.route('/showFavorityFlower')
# def flower():

#     return render_template ("flower.html", flower=rose )


if __name__ == "__main__": 
    app.run(port=5000, debug=True)