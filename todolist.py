from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    _id = db.Column(db.Integer, primary_key = True)
    Task = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    todos = Todo.query.all()

    return render_template('index.html', todos = todos)

@app.route('/add', methods = ['POST'])
def add():
    todo = Todo(Task = request.form['todoitem'], complete = False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
     todo = Todo.query.filter_by(_id = int(id)).first()
     db.session.delete(todo)
     db.session.commit()
     return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)