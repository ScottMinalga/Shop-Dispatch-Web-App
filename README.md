Shop Dispatch Web App
Shop Dispatch is a web application that allows users to manage projects and parts in the 2 different assembly departments in the manufacturing process.

Features
Add, edit, and delete projects
Add, edit, and delete parts
View a list of all parts
Admin and login systems

Installation
Clone the repository: git clone https://github.com/ScottMinalga/Shop-Dispatch-Web-App.git
Install dependencies: pip install -r requirements.txt
Create a database: python manage.py createdb

Configuration
Create a .env file in the project root directory.
Set the following environment variables in the .env file:
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://user:password@localhost/asm

Usage
Start the application: flask run
Open a web browser and navigate to http://localhost:5000
Log in using your username and password
Use the navigation menu to add, edit, and view projects and parts

Contributing
If you encounter any bugs or have feature requests, please submit an issue on the project's GitHub repository. Pull requests are also welcome.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Credits
This project uses the following third-party libraries:

Flask
SQLAlchemy
WTForms
Bootstrap

Author
Scott Minalga Scott.Minalga@gmail.com
