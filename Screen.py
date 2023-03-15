from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects/sql.db'

db = SQLAlchemy(app)

class projects(db.Model):
    id = db.Column('database_id' , db.Integer, primary_key = True)
    projectnum = db.Column(db.String(50))
    jobnum = db.Column(db.String(50))
    salesnum = db.Column(db.String(50))
    customername = db.Column(db.String(100))
    builder = db.Column(db.String(50))
    status = db.Column(db.String(50))

def __init__(self, projectnum, jobnum, salesnum, customername, builder, status):
    self.projectnum = projectnum
    self.jobnum = jobnum
    self.salesnum = salesnum
    self.customername = customername
    self.builder = builder
    self.status = status

@app.route('/')
def table():
    return render_template('show_all.html')

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == "POST":
        if not request.form['projectnum'] or not request.form['jobnum'] or not request.form['salesnum'] or not request.form['customername']:
            flash(f'Please enter all the fields----ERROR')
        else:
            project = projects(request.form['projectnum'], request.form['jobnum'],
                request.form['salesnum'], request.form['customername'], request.form['builder'], request.form['status'])

            db.session.add(project)
            db.session.commit()
            flash(f"Project was successfully added")
            return redirect(url_for('table'))
    return render_template('new.html')

with app.app_context():
    db.create_all()
    app.run(debug = True)

