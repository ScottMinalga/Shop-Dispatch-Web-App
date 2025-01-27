from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired
from sqlalchemy import Column, Integer
import csv


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
    due_date = db.Column(db.String(100))
    order_date = db.Column(db.String(100))
    ship_date = db.Column(db.String(100))
    order_quantity = db.Column(db.String(100))
    order = db.Column(db.Integer)

    def __init__(self, project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity, order):
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
        self.order = order

    def to_dict(self):
        return {
            'project_number': self.project_number,
            'job_number': self.job_number,
            'sales_order': self.sales_order,
            'customer_name': self.customer_name,
            'builder': self.builder,
            'status': self.status,
            'notes': self.notes,
            'due_date': self.due_date,
            'order_date': self.order_date,
            'ship_date': self.ship_date,
            'order_quantity': self.order_quantity,
        }


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
    order = db.Column(db.Integer)

    def __init__(self, project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity, order):
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
        self.order = order

    def to_dict(self):
        return {
            'project_number': self.project_number,
            'job_number': self.job_number,
            'sales_order': self.sales_order,
            'customer_name': self.customer_name,
            'builder': self.builder,
            'status': self.status,
            'notes': self.notes,
            'due_date': self.due_date,
            'order_date': self.order_date,
            'ship_date': self.ship_date,
            'order_quantity': self.order_quantity,
        }

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
    order = db.Column(db.Integer)

    def __init__(self, project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity, order):
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
        self.order = order

    def to_dict(self):
        return {
            'project_number': self.project_number,
            'job_number': self.job_number,
            'sales_order': self.sales_order,
            'customer_name': self.customer_name,
            'builder': self.builder,
            'status': self.status,
            'notes': self.notes,
            'due_date': self.due_date,
            'order_date': self.order_date,
            'ship_date': self.ship_date,
            'order_quantity': self.order_quantity,
        }

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
    ASM01_data = ASM01.query.order_by(ASM01.order.asc()).all()
    ASM02_data = ASM02.query.order_by(ASM02.order.asc()).all()
    archive_data = archive.query.order_by(archive.order.asc()).all()

    all_parts = parts.query.all()
    parts_job_numbers = {part.job_number for part in all_parts}

    is_logged_in = "username" in session  # Determine login status

    return render_template(
        'render_table_with_tabs.html',
        ASM01_data=ASM01_data,
        ASM02_data=ASM02_data,
        archive_data=archive_data,
        parts_job_numbers=parts_job_numbers,
        is_logged_in=is_logged_in,
    )



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

        # Retrieve form data
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

        # Calculate the `order` value dynamically (default to 0 if no rows exist)
        if target_table == 'ASM01-tab':
            last_entry = ASM01.query.order_by(ASM01.order.desc()).first()
            order = (last_entry.order + 1) if last_entry else 0

            new_job01 = ASM01(project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity, order)
            db.session.add(new_job01)
            db.session.commit()
            flash("Job added successfully!")
            ASM01_data = ASM01.query.all()
            return render_template("new.html", ASM01_data=ASM01_data, ASM02_data=ASM02_data, archive_data=archive_data)

        elif target_table == 'ASM02-tab':
            last_entry = ASM02.query.order_by(ASM02.order.desc()).first()
            order = (last_entry.order + 1) if last_entry else 0

            new_job02 = ASM02(project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity, order)
            db.session.add(new_job02)
            db.session.commit()
            flash("Job added successfully!")
            ASM02_data = ASM02.query.all()
            return render_template("new.html", ASM01_data=ASM01_data, ASM02_data=ASM02_data, archive_data=archive_data)

        elif target_table == 'archive-tab':
            last_entry = archive.query.order_by(archive.order.desc()).first()
            order = (last_entry.order + 1) if last_entry else 0

            new_jobA = archive(project_number, job_number, sales_order, customer_name, builder, status, notes, due_date, order_date, ship_date, order_quantity, order)
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

@app.route('/parts/<part_number>/edit', methods=['GET'])
def edit_part(part_number):
    part = parts.query.get_or_404(part_number)
    form = EditPartForm(obj=part)  # Assuming you have a form for editing a part
    return render_template('edit_part.html', form=form)

def to_dict(self):
    return {
        'part_number': self.part_number,
        'project_number': self.project_number,
        'job_number': self.job_number,
        'sales_order': self.sales_order,
        'vendor_name': self.vendor_name,
        'status': self.status,
        'notes': self.notes,
        'ship_date': self.ship_date.isoformat() if self.ship_date else None,
        'order_quantity': self.order_quantity,
        'order_date': self.order_date.isoformat() if self.order_date else None,
        'received_date': self.received_date.isoformat() if self.received_date else None,
    }

# Delete a part
@app.route('/parts/<part_number>', methods=['DELETE'])
def delete_part(part_number):
    part = parts.query.filter_by(part_number=part_number).first_or_404()
    db.session.delete(part)
    db.session.commit()
    return jsonify({'message': 'Part deleted successfully'})

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

# Route to return all jobs from ASM01, ASM02, and archive in JSON format
@app.route('/api/jobs', methods=['GET'])
def get_all_jobs():
    asm01_jobs = ASM01.query.all()
    asm02_jobs = ASM02.query.all()
    archive_jobs = archive.query.all()

    # Convert data to list of dictionaries
    asm01_data = [job.__dict__ for job in asm01_jobs]
    asm02_data = [job.__dict__ for job in asm02_jobs]
    archive_data = [job.__dict__ for job in archive_jobs]

    # Remove the SQLAlchemy state information that isn't JSON serializable
    for job in asm01_data + asm02_data + archive_data:
        job.pop('_sa_instance_state', None)

    return jsonify({
        'asm01_jobs': asm01_data,
        'asm02_jobs': asm02_data,
        'archive_jobs': archive_data
    })

# Route to return a specific job from ASM01, ASM02, or archive by job_number
@app.route('/api/jobs/<string:job_number>', methods=['GET'])
def get_job(job_number):
    # Search in all job tables for the job_number
    job = ASM01.query.filter_by(job_number=job_number).first() or \
          ASM02.query.filter_by(job_number=job_number).first() or \
          archive.query.filter_by(job_number=job_number).first()

    if not job:
        return jsonify({'error': 'Job not found'}), 404

    # Convert job to dictionary and remove SQLAlchemy state information
    job_data = job.__dict__
    job_data.pop('_sa_instance_state', None)

    return jsonify(job_data)


@app.route('/get_entry_data', methods=['GET'])
def get_entry_data():
    job_number = request.args.get('jobNumber')
    entry = (
        ASM01.query.filter_by(job_number=job_number).first()
        or ASM02.query.filter_by(job_number=job_number).first()
        or archive.query.filter_by(job_number=job_number).first()
    )
    if not entry:
        return jsonify({'error': 'Entry not found'}), 404
    
    return jsonify({
        'project_number': entry.project_number,
        'job_number': entry.job_number,
        'sales_order': entry.sales_order,
        'customer_name': entry.customer_name,
        'builder': entry.builder,
        'status': entry.status,
        'notes': entry.notes,
        'due_date': entry.due_date,
        'order_date': entry.order_date,
        'ship_date': entry.ship_date,
        'order_quantity': entry.order_quantity,
    })


@app.route('/change_table', methods=['POST'])
def change_table():
    job_number = request.form.get('job_number')
    new_table_name = request.form.get('new_table_name')

    if not job_number:
        return jsonify({'success': False, 'message': 'Job number is missing.'}), 400
    if not new_table_name:
        return jsonify({'success': False, 'message': 'Table name is missing.'}), 400

    try:
        # Fetch the entry from the current table
        entry = ASM01.query.filter_by(job_number=job_number).first() or \
                ASM02.query.filter_by(job_number=job_number).first() or \
                archive.query.filter_by(job_number=job_number).first()

        if not entry:
            return jsonify({'success': False, 'message': 'Entry not found.'}), 404

        # Convert entry to dictionary and include the order field
        entry_data = entry.to_dict()
        entry_data['order'] = entry.order  # Explicitly add the 'order' field

        # Remove entry from the current table and add it to the new table
        if new_table_name == "ASM01":
            db.session.add(ASM01(**entry_data))
        elif new_table_name == "ASM02":
            db.session.add(ASM02(**entry_data))
        elif new_table_name == "archive":
            db.session.add(archive(**entry_data))
        else:
            return jsonify({'success': False, 'message': 'Invalid table name provided.'}), 400

        db.session.delete(entry)
        db.session.commit()

        return jsonify({'success': True, 'message': f'Entry moved to {new_table_name} successfully!'})
    except Exception as e:
        db.session.rollback()
        print(f"Error moving entry: {e}")
        return jsonify({'success': False, 'message': 'Failed to move entry. Please try again later.'}), 500

@app.route('/delete_entry', methods=['POST'])
def delete_entry():
    job_number = request.form.get('job_number')

    if not job_number:
        return jsonify({'status': 'error', 'message': 'Job number is missing.'}), 400

    # Try to find this job in ASM01 or ASM02
    entry = ASM01.query.filter_by(job_number=job_number).first() \
            or ASM02.query.filter_by(job_number=job_number).first()

    if not entry:
        return jsonify({'status': 'error', 'message': 'Entry not found.'}), 404

    try:
        # Move the entry to the archive (make sure to include 'order=entry.order')
        archived_entry = archive(
            project_number=entry.project_number,
            job_number=entry.job_number,
            sales_order=entry.sales_order,
            customer_name=entry.customer_name,
            builder=entry.builder,
            status=entry.status,
            notes=entry.notes,
            due_date=entry.due_date,
            order_date=entry.order_date,
            ship_date=entry.ship_date,
            order_quantity=entry.order_quantity,
            order=entry.order  # <-- IMPORTANT
        )
        db.session.add(archived_entry)

        # Now remove it from the original table
        db.session.delete(entry)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Entry moved to archive successfully!'})
    except Exception as e:
        db.session.rollback()
        print(f"Error archiving entry: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to archive entry.'}), 500


@app.route('/update_entry', methods=['POST'])
def update_entry():
    try:
        print("Received form data:", request.form)  # Debug log
        job_number = request.form.get('jobNumber')

        if not job_number:
            return jsonify({'error': 'jobNumber is missing'}), 400

        entry = ASM01.query.filter_by(job_number=job_number).first() or \
                ASM02.query.filter_by(job_number=job_number).first() or \
                archive.query.filter_by(job_number=job_number).first()

        if not entry:
            return jsonify({'error': f'Entry with job number {job_number} not found'}), 404

        # Update fields from the form
        entry.project_number = request.form.get('project_number')
        entry.sales_order = request.form.get('sales_order')
        entry.customer_name = request.form.get('customer_name')
        entry.builder = request.form.get('builder')
        entry.status = request.form.get('status')
        entry.notes = request.form.get('notes')
        entry.due_date = request.form.get('due_date')
        entry.order_date = request.form.get('order_date')
        entry.ship_date = request.form.get('ship_date')
        entry.order_quantity = request.form.get('order_quantity')

        print(f"Updating entry: {entry.__dict__}")  # Log updated entry data
        db.session.commit()
        return jsonify({'message': 'Entry updated successfully!'})
    except Exception as e:
        print(f"Error during update: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to update entry'}), 500

@app.route("/update_order", methods=["POST"])
def update_order():
    try:
        data = request.get_json()            # JSON: { "order": [ { "job_number": "X", "order": 0 }, ... ] }
        order_list = data.get("order", [])   # Extract the list

        for item in order_list:
            job_number = item["job_number"]
            new_order = item["order"]
            
            # Find the matching record in ASM01 or ASM02 or archive
            entry = (ASM01.query.filter_by(job_number=job_number).first()
                     or ASM02.query.filter_by(job_number=job_number).first()
                     or archive.query.filter_by(job_number=job_number).first())
            
            if entry:
                entry.order = new_order  # assign the new order

        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/update_part", methods=['POST'])
def update_part():
    # Because we're sending form data (not JSON) from JS:
    part_number = request.form.get('part_number')
    if not part_number:
        return jsonify({'success': False, 'message': 'No part_number provided'}), 400

    part = parts.query.filter_by(part_number=part_number).first()
    if not part:
        return jsonify({'success': False, 'message': f'Part {part_number} not found'}), 404

    # Update all fields from the request
    part.project_number = request.form.get('project_number')
    part.job_number = request.form.get('job_number')
    part.sales_order = request.form.get('sales_order')
    part.vendor_name = request.form.get('vendor_name')
    part.status = request.form.get('status')
    part.notes = request.form.get('notes')
    part.ship_date = request.form.get('ship_date')
    part.order_quantity = request.form.get('order_quantity')

    db.session.commit()
    return jsonify({'success': True, 'message': 'Part updated successfully'})

@app.route("/upload_csv", methods=["GET", "POST"])
def upload_csv():
    if request.method == "POST":
        # 1. Check if the file is in the request
        if "csv_file" not in request.files:
            flash("No file part in the request.", "danger")
            return redirect(url_for("upload_csv"))
        
        file = request.files["csv_file"]
        if file.filename == "":
            flash("No selected file.", "danger")
            return redirect(url_for("upload_csv"))
        
        # 2. Parse the CSV
        try:
            # file.stream is an open file object
            csv_reader = csv.DictReader(file.stream)  
            
            rows_added = 0
            for row in csv_reader:
                # row is a dictionary with keys = CSV header columns
                # e.g. row["part_number"], row["job_number"], etc.

                # Create a new `parts` object (assuming your model is named `parts`)
                new_part = parts(
                    part_number = row["part_number"],
                    project_number = row["project_number"],
                    job_number = row["job_number"],
                    sales_order = row["sales_order"],
                    vendor_name = row["vendor_name"],
                    status = row["status"],
                    notes = row["notes"],
                    ship_date = row["ship_date"],
                    order_quantity = row["order_quantity"],
                    order_date = row["order_date"],
                    received_date = row["received_date"]
                )

                db.session.add(new_part)
                rows_added += 1

            db.session.commit()
            flash(f"CSV imported successfully! {rows_added} records added.", "success")
            return redirect(url_for("view_parts"))
        
        except Exception as e:
            flash(f"Error importing CSV: {e}", "danger")
            return redirect(url_for("upload_csv"))
    
    # If GET, just show the form
    return render_template("upload_csv.html")

@app.route('/view_users', methods=['GET'])
@admin_required
def view_users():
    # Query all users from the database
    users = User.query.all()
    
    # Render the template with the users data
    return render_template('view_users.html', users=users)


with app.app_context():
    if not hasattr(ASM01, 'order'):
        try:
            db.engine.execute('ALTER TABLE asm01 ADD COLUMN "order" INTEGER DEFAULT 0')
        except Exception as e:
            print(f"Column 'order' might already exist in ASM01: {e}")

    if not hasattr(ASM02, 'order'):
        try:
            db.engine.execute('ALTER TABLE asm02 ADD COLUMN "order" INTEGER DEFAULT 0')
        except Exception as e:
            print(f"Column 'order' might already exist in ASM02: {e}")

    if not hasattr(archive, 'order'):
        try:
            db.engine.execute('ALTER TABLE archive ADD COLUMN "order" INTEGER DEFAULT 0')
        except Exception as e:
            print(f"Column 'order' might already exist in archive: {e}")

    db.session.commit()



#run the app and creates db database if not already done
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_initial_admin()
    app.run(host="10.120.108.19", port=5000, debug=True)
