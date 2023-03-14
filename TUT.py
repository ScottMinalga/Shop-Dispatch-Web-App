from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)



@app.route('/')
def index():
    return print("Hello Team")

@app.route("/add", methods=["POST"])
def add():
    # add new item
    title = request.form.get("Project Number")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/submit')
def about():
    #Show all todos
    todo_list = Todo.querry.all()
    return render_template('Submit.html', todo_list=todo_list)

if __name__ == "__main__":
    db.create_all()

    new_todo = Todo(title="todo_1", complete=False)
    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True)