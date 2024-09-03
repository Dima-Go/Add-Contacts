## Contacts App 
This is a Flask-based web application for managing contacts. The application supports both SQL (MySQL) and NoSQL (MongoDB) databases, allowing you to store, retrieve, update, and delete contact information. The application features a form for adding contacts, viewing all contacts, editing contacts, and searching for specific contacts by name.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Use](#use)
- [Installation](#installation)
- [Screenshots](#Screenshots)
- [License](#license)
- [Contact](#contact)

## Features
- Add new contacts with details such as name, phone, email, gender, and photo.
- View a list of all contacts.
- Search contacts by name.
- Edit contact details.
- Delete contacts.
- Supports both MySQL and MongoDB databases.

## Requirements
- Python 3.7+
- Flask
- MySQL
- MongoDB
- pymongo
- mysql-connector-python
- python-dotenv

## Project Structure
- "app.py" - The main application file with routes.
- 'data_sql.py' - Functions for MySQL database operations.
- 'data_mongo.py' - Functions for MongoDB database operations.
- 'templates/' - HTML templates for rendering pages.
- 'static/images/' - Directory for storing contact photos.
- 'static/style/' - Directory for CSS files.
- 'static/js/' - Directory for JavaScript files.
- '.env' - Environment configuration file.
- 'requirements.txt' - Python dependencies.

## Setup
1. Create a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
2. Install Dependencies
    pip install -r requirements.txt
    python3 migrations.py
3. Configure Environment Variables
Create a .env file in the root directory of the project and add your database configuration
   # MySQL Configuration:
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=admin
    DB_NAME=contacts_app2
    DB_PORT=3306
   # MongoDB Configuration (used if DATABASE_TYPE is set to mongo)
    MONGO_URI=mongodb://localhost:27017/
    DATABASE_TYPE=mongo  # Set to either "sql" for MySQL or "mongo" for MongoDB
4. Initialize the Database
    # For MySQL:
    Ensure MySQL is running and properly configured.
    The database and table creation are handled automatically by the create_db and create_contacts_table functions in the data_sql.py file.
    Run the application, and the database and tables will be created automatically.
    # For MongoDB:
    Ensure MongoDB is running.
    The MongoDB database and collections are created automatically when inserting data via the application.

## Usage
   # Running the app
1. Activate your virtual environment if it's not already activated.
2. Run the Flask application:
    python3 app.py 
3. Access the application at http://localhost:5000. 

    # Routes
* /form - Add a new contact.
* /contacts - View all contacts.
* /addContact - Create a new contact (POST).
* /deleteContact/<number> - Delete a contact by number or _id.
* /editContact/<number> - Edit an existing contact.
* /saveUpdatedContact/<number> - Save updates to a contact (POST).
* /search - Search for contacts by name (POST).

    # Switching Between MySQL and MongoDB
To switch between using MySQL and MongoDB, update the DATABASE_TYPE in your .env file:
    DATABASE_TYPE=sql  # For MySQL
    DATABASE_TYPE=mongo  # For MongoDB

## License
This project is licensed under the MIT License.

## Contact
dimitrygolde@gmail.com
