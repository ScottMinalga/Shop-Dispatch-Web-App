from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

#create instance of the app
app = Flask(__name__)
app.secret_key = "marubeni"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHENY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=120)


db = SQLAlchemy(app)

#model for SQL
class projects(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    project_number = db.Column(db.String(100))
    job_number = db.Column(db.String(100))
    sales_order = db.Column(db.String(100))
    customer_name = db.Column(db.String(100))
    builder = db.Column(db.String(100))
    status = db.Column(db.String(100))
    notes = db.Column(db.String(500))



    def __init__(self, project_number, job_number, sales_order, customer_name, builder, status, notes):
        self.project_number = project_number
        self.job_number = job_number
        self.sales_order = sales_order
        self.customer_name = customer_name
        self.builder = builder
        self.status = status
        self.notes = notes


# we can use html to pass variable through
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user,"")
            db.session.add(usr)
            db.session.commit()

        flash("Login Succesful")
        return redirect(url_for("user"))       
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
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
    
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

#run the app and creats db database if not already done
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)