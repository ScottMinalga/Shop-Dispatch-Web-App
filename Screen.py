from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired

# Create instance of the app
app = Flask(__name__)
app.secret_key = "marubeni"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=120)

db = SQLAlchemy(app)

#model for SQL

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
    part_number = db.Column(db.String(100))
    project_number = db.Column(db.String(100))
    job_number = db.Column(db.String(100))
    sales_order = db.Column(db.String(100))
    vendor_name = db.Column(db.String(100))
    status = db.Column(db.String(100))
    notes = db.Column(db.String(500))
    ship_date = db.Column(db.String(100))
    order_quantity = db.Column(db.String(100))
    order_date = db.Column(db.String(100))
    received_date = db.Column(db.String(100))

    def __init__(self,part_number, project_number, job_number, sales_order, vendor_name, status, notes, ship_date, order_quantity, order_date, received_date):
        self.part_number = part_number
        self.project_number = project_number
        self.job_number = job_number
        self.sales_order = sales_order
        self.vendor_name = vendor_name
        self.status = status
        self.notes = notes
        self.ship_date = ship_date
        self.order_quantity = order_quantity
        self.order_date = order_date
        self.received_date = received_date

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
    
class AddPartForm(FlaskForm):
    order_date = DateField('Order Date', validators=[DataRequired()])
    received_date = DateField('Received Date', validators=[DataRequired()])
    ship_date = DateField('Ship Date', validators=[DataRequired()])
    part_number = StringField('Part Number', validators=[DataRequired()])
    project_number = StringField('Project Number', validators=[DataRequired()])
    job_number = StringField('Job Number', validators=[DataRequired()])
    sales_order = StringField('Sales Order', validators=[DataRequired()])
    vendor_name = StringField('Vendor Name', validators=[DataRequired()])
    status = SelectField('Status', choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2'), ('choice3', 'Choice 3')])
    order_quantity = IntegerField('Order Quantity', validators=[DataRequired()])
    notes = TextAreaField('Notes')


# we can use html to pass variable through
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    ASM01_data = ASM01.query.all()
    ASM02_data = ASM02.query.all()
    archive_data = archive.query.all()

    # Sort the data by 'ship_date'
    ASM01_data = sorted(ASM01_data, key=lambda x: x.ship_date)
    ASM02_data = sorted(ASM02_data, key=lambda x: x.ship_date)
    archive_data = sorted(archive_data, key=lambda x: x.ship_date)

    # Get all parts and create a set of unique job numbers
    all_parts = parts.query.all()
    parts_job_numbers = {part.job_number for part in all_parts}

    print(ASM01_data, ASM02_data, archive_data, parts_job_numbers)

    return render_template(
        'render_table_with_tabs.html',
        ASM01_data=ASM01_data,
        ASM02_data=ASM02_data,
        archive_data=archive_data,
        parts_job_numbers=parts_job_numbers,
    )

@app.route('/edit_entry/<table_name>/<int:entry_id>', methods=['POST'])
def edit_entry(table_name, entry_id):
    entry = get_entry_by_id(table_name, entry_id)
    if entry is None:
        abort(404)
    # Update the entry with the form data
    form_data = request.form
    entry.project_number = form_data['projectnum']
    entry.job_number = form_data['jobnum']
    entry.sales_order = form_data['salesnum']
    # Add more fields as needed
    db.session.commit()
    # Return the updated entry data as a JSON response
    return jsonify({
        'id': entry.id,
        'project_number': entry.project_number,
        'job_number': entry.job_number,
        'sales_order': entry.sales_order,
        # Add more fields as needed
    })


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

def has_matching_job_number(parts, job_number):
    for part in parts:
        if part.job_number == job_number:
            return True
    return False


app.jinja_env.filters['has_matching_job_number'] = has_matching_job_number
    
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
    
    
@app.route("/add", methods=["POST", "GET"])
@admin_required
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
   
@app.route("/add_part", methods=["GET", "POST"])
@admin_required
def add_part():
    form = AddPartForm()
    if request.method == "POST":
        part_number = request.form["part_number"]
        project_number = request.form["project_number"]
        job_number = request.form["job_number"]
        sales_order = request.form["sales_order"]
        vendor_name = request.form["vendor_name"]
        status = request.form["status"]
        notes = request.form["notes"]
        ship_date = request.form["ship_date"]
        order_quantity = request.form["order_quantity"]
        order_date = request.form["order_date"]
        received_date = request.form["received_date"]

        part = parts(part_number, project_number, job_number, sales_order, vendor_name, status, notes, ship_date, order_quantity, order_date, received_date)

        db.session.add(part)
        db.session.commit()

        flash("Part added successfully!")
        return redirect(url_for("add_part"))

    return render_template("add_part.html", form=form)

@app.route("/view_parts")
@app.route("/view_parts/<job_number>")
def view_parts(job_number=None):
    if job_number:
        all_parts = parts.query.filter_by(job_number=job_number).all()
    else:
        all_parts = parts.query.all()
    return render_template("view_parts.html", parts=all_parts)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

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

