from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Create instance of the app
app = Flask(__name__)
app.secret_key = "marubeni"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=120)

db = SQLAlchemy(app)

#model for SQL
class ASM02(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    project_number = db.Column(db.String(100))
    job_number = db.Column(db.String(100))
    sales_order = db.Column(db.String(100))
    customer_name = db.Column(db.String(100))
    builder = db.Column(db.String(100))
    status = db.Column(db.String(100))
    notes = db.Column(db.String(500))
    due_date =db.Column(db.String(100))
    order_date = db.Column(db.String(100))
    ship_date = db.Column(db.String(100))
    order_quantity = db.Column(db.String(100))



    def __init__(self, project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity):
        self.project_number = project_number
        self.job_number = job_number
        self.sales_order = sales_order
        self.customer_name = customer_name
        self.builder = builder
        self.status = status
        self.notes = notes
        self.due_date = due_date
        self.order_date = order_date
        self.ship_date = ship_date
        self.order_quantity = order_quantity

class ASM01(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    project_number = db.Column(db.String(100))
    job_number = db.Column(db.String(100))
    sales_order = db.Column(db.String(100))
    customer_name = db.Column(db.String(100))
    builder = db.Column(db.String(100))
    status = db.Column(db.String(100))
    notes = db.Column(db.String(500))
    due_date =db.Column(db.String(100))
    order_date = db.Column(db.String(100))
    ship_date = db.Column(db.String(100))
    order_quantity = db.Column(db.String(100))



    def __init__(self, project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity):
        self.project_number = project_number
        self.job_number = job_number
        self.sales_order = sales_order
        self.customer_name = customer_name
        self.builder = builder
        self.status = status
        self.notes = notes
        self.due_date = due_date
        self.order_date = order_date
        self.ship_date = ship_date
        self.order_quantity = order_quantity

class archive(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    project_number = db.Column(db.String(100))
    job_number = db.Column(db.String(100))
    sales_order = db.Column(db.String(100))
    customer_name = db.Column(db.String(100))
    builder = db.Column(db.String(100))
    status = db.Column(db.String(100))
    notes = db.Column(db.String(500))
    due_date =db.Column(db.String(100))
    order_date = db.Column(db.String(100))
    ship_date = db.Column(db.String(100))
    order_quantity = db.Column(db.String(100))



    def __init__(self, project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity):
        self.project_number = project_number
        self.job_number = job_number
        self.sales_order = sales_order
        self.customer_name = customer_name
        self.builder = builder
        self.status = status
        self.notes = notes
        self.due_date = due_date
        self.order_date = order_date
        self.ship_date = ship_date
        self.order_quantity = order_quantity

class parts(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    project_number = db.Column(db.String(100))
    job_number = db.Column(db.String(100))
    sales_order = db.Column(db.String(100))
    vendor_name = db.Column(db.String(100))
    status = db.Column(db.String(100))
    notes = db.Column(db.String(500))
    ship_date = db.Column(db.String(100))
    order_quantity = db.Column(db.String(100))

    def __init__(self, project_number, job_number, sales_order, vendor_name, status, notes, ship_date, order_quantity):
        self.project_number = project_number
        self.job_number = job_number
        self.sales_order = sales_order
        self.vendor_name = vendor_name
        self.status = status
        self.notes = notes
        self.ship_date = ship_date
        self.order_quantity = order_quantity

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


# we can use html to pass variable through
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    ASM01_data = ASM01.query.all()
    ASM02_data = ASM02.query.all()
    archive_data = archive.query.all()
    return render_template('render_table_with_tabs.html', ASM01_data=ASM01_data, ASM02_data=ASM02_data, archive_data=archive_data)

@app.route("/edit/<string:table_name>/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(table_name, entry_id):
    if table_name == "ASM01":
        model_class = ASM01
    elif table_name == "ASM02":
        model_class = ASM02
    elif table_name == "archive":
        model_class = archive
    else:
        flash("Invalid table name.")
        return redirect(url_for("view"))

    entry = model_class.query.get_or_404(entry_id)

    if request.method == "GET":
        return render_template("edit.html", entry=entry)

    if request.method == "POST":
        entry.project_number = request.form["projectnum"]
        entry.job_number = request.form["jobnum"]
        entry.sales_order = request.form["salesnum"]
        entry.customer_name = request.form["customername"]
        entry.builder = request.form["builder"]
        entry.status = request.form["status"]
        entry.notes = request.form["notes"]
        entry.due_date = request.form["due_date"]
        entry.order_date = request.form["order_date"]
        entry.ship_date = request.form["ship_date"]
        entry.order_quantity = request.form["order_quantity"]

        db.session.commit()
        flash("Entry updated successfully!")
        return redirect(url_for("view"))

    return render_template("edit.html", entry=entry)


@app.route("/delete/<string:table_name>/<int:entry_id>")
def delete_entry(table_name, entry_id):
    if table_name == "ASM01":
        model_class = ASM01
    elif table_name == "ASM02":
        model_class = ASM02
    elif table_name == "archive":
        model_class = archive
    else:
        flash("Invalid table name.")
        return redirect(url_for("view"))

    entry = model_class.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted successfully!")
    return redirect(url_for("view"))

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "username" in session:
        username = session["username"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = User.query.filter_by(username=username).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/add", methods=["POST", "GET"])
def add():
    ASM01_data = ASM01.query.all()
    ASM02_data = ASM02.query.all()
    archive_data = archive.query.all()

    if request.method == 'POST':
        target_table = request.form['target_table']
        
        if target_table == 'ASM01-tab':
            project_number = request.form["projectnum"]
            job_number = request.form["jobnum"]
            sales_order = request.form["salesnum"]
            customer_name = request.form["customername"]
            builder = request.form["builder"]
            status = request.form["status"]
            order_quantity = request.form["order_quantity"]
            due_date = request.form["due_date"]
            order_date = request.form["order_date"]
            ship_date = request.form["ship_date"]
            notes = request.form["notes"]

            new_job01 = ASM01(project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity)
            db.session.add(new_job01)
            db.session.commit()
            flash("Job added successfully!")
            ASM01_data = ASM01.query.all()
            return render_template("new.html", ASM01_data=ASM01_data, ASM02_data=ASM02_data, archive_data=archive_data)
        
        elif target_table == 'ASM02-tab':
            project_number = request.form["projectnum"]
            job_number = request.form["jobnum"]
            sales_order = request.form["salesnum"]
            customer_name = request.form["customername"]
            builder = request.form["builder"]
            status = request.form["status"]
            order_quantity = request.form["order_quantity"]
            due_date = request.form["due_date"]
            order_date = request.form["order_date"]
            ship_date = request.form["ship_date"]
            notes = request.form["notes"]

            new_job02 = ASM02(project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity)
            db.session.add(new_job02)
            db.session.commit()
            flash("Job added successfully!")
            ASM02_data = ASM02.query.all()
            return render_template("new.html", ASM01_data=ASM01_data, ASM02_data=ASM02_data, archive_data=archive_data)
        
        elif target_table == 'archive-tab':
            project_number = request.form["projectnum"]
            job_number = request.form["jobnum"]
            sales_order = request.form["salesnum"]
            customer_name = request.form["customername"]
            builder = request.form["builder"]
            status = request.form["status"]
            order_quantity = request.form["order_quantity"]
            due_date = request.form["due_date"]
            order_date = request.form["order_date"]
            ship_date = request.form["ship_date"]
            notes = request.form["notes"]

            new_jobA = archive(project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity)
            db.session.add(new_jobA)
            db.session.commit()
            flash("Job added successfully!")
            archive_data = archive.query.all()
            return render_template("new.html", ASM01_data=ASM01_data, ASM02_data=ASM02_data, archive_data=archive_data)
        
        else:
            # Handle invalid input
            flash("Error, Try Again, Make sure you fill out the form correctly, If you keep getting error please see system admin")
            return redirect(url_for('add'))

    return render_template("new.html", ASM01_data=ASM01_data, ASM02_data=ASM02_data, archive_data=archive_data)
   
@app.route("/logout")
def logout():
    if "username" in session:
        username = session["username"]
        flash(f"You have been logged out, {username}!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            flash("You need to be logged in to access this page.", "danger")
            return redirect(url_for("login"))
        user = User.query.filter_by(username=session["username"]).first()
        if not user.is_admin:
            flash("You don't have permission to access this page.", "danger")
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/admin")
@admin_required
def admin():
    return render_template("admin.html")

@app.route('/add_user', methods=['POST'])
@admin_required
def add_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    is_admin = 'is_admin' in request.form

    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        flash('Username or email already exists.', 'danger')
        return redirect(url_for('admin'))

    new_user = User(username=username, email=email, password=password)
    new_user.is_admin = is_admin
    db.session.add(new_user)
    db.session.commit()

    flash('User added successfully.', 'success')
    return redirect(url_for('admin'))

def create_initial_admin():
    # Set your admin user's details
    admin_username = "SMinalga"
    admin_email = "Admin@email.com"
    admin_password = "ScottyAdmin"

    # Check if an admin user already exists
    existing_admin = User.query.filter_by(username=admin_username).first()

    if not existing_admin:
        # Create the admin user
        admin_user = User(username=admin_username, email=admin_email, password=admin_password)
        admin_user.is_admin = True
        db.session.add(admin_user)
        db.session.commit()

        print("Initial admin user created.")
    else:
        print("An admin user already exists.")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user._id
            session['username'] = user.username
            session['is_admin'] = user.is_admin

            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password. Please try again.', 'danger')

    return render_template('login.html')

#run the app and creates db database if not already done
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_initial_admin()
    app.run(debug=True)

