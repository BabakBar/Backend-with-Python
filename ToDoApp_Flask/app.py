from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# a class to inherit from db.Model with 3 columns & data types
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

db.create_all()

@app.get("/")
def home():
    # todo_list = Todo.query.all()
    todo_list = db.session.query(Todo).all()
    return render_template("base.html", todo_list=todo_list)


# @app.route("/add", methods=["POST"])
@app.post("/add")
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/') #decorator - homepage
def index():    # assign a method - response to request
    return 'Hello from Sia!'

app.run(port=5000)