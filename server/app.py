import os
import subprocess
from sqlalchemy import create_engine
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost') # 'mysql'
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PORT = os.environ.get('MYSQL_PORT', '3306')
# MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '123456')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'HansaSpiti2008')
MYSQL_DB = os.environ.get('MYSQL_DB', 'devops_p1')

# Grant privileges to the mysql user with subprocess
# subprocess.call(f'mysql -h {MYSQL_HOST} -u root -p{MYSQL_PASSWORD} -e "GRANT ALL PRIVILEGES ON {MYSQL_DB}.* TO \'{MYSQL_USER}\'@\'%\' IDENTIFIED BY \'{MYSQL_PASSWORD}\';"', shell=True)

# subprocess.call(f'mysql -h {MYSQL_HOST} -u root -p{MYSQL_PASSWORD} -e "GRANT ALL PRIVILEGES ON {MYSQL_DB}.* TO \'{MYSQL_USER}\'@\'*\' IDENTIFIED BY \'{MYSQL_PASSWORD}\';"', shell=True)
# subprocess.call(f'mysql -h * -u root -p{MYSQL_PASSWORD} -e "GRANT ALL PRIVILEGES ON * TO \'{MYSQL_USER}\'@\'*\' IDENTIFIED BY \'{MYSQL_PASSWORD}\';"', shell=True)
# subprocess.call(f'mysql -h {MYSQL_HOST} -u root -p{MYSQL_PASSWORD} -e "GRANT ALL PRIVILEGES ON *.* TO \'{MYSQL_USER}\'@\'%\' IDENTIFIED BY \'{MYSQL_PASSWORD}\';"', shell=True)




# create database user and grant privileges to all hosts
# engine = create_engine(f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}')
# with engine.connect() as con:
#     con.execute("GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';")

# engine = create_engine(f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@mysql:{MYSQL_PORT}')
# with engine.connect() as con:
#      con.execute("GRANT ALL PRIVILEGES ON *.* TO 'root'@'*';")


# Databse configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

ma=Marshmallow(app)

class Todos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime,default=datetime.datetime.now)

    def __init__(self,title,body):
        self.title=title
        self.body=body


class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id','title','body','date')

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

with app.app_context():
    db.create_all()


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def serve(path):
#     if path != "" and os.path.exists("static/" + path):
#         return send_from_directory('static', path)
#     else:
#         return send_from_directory('static', 'index.html')

@app.route("/")
def my_index():
    return render_template("index.html", flask_token="Hello Flask+React")


# @desc      Get all todos
# @rout      GET /todos
# @access    Public
@app.route('/todos',methods =['GET'])
def get_todos():
    all_todos = Todos.query.all()
    results = todos_schema.dump(all_todos)
    return jsonify(results)

# @desc      Get single todo
# @rout      GET /todos/<id>
# @access    Public
@app.route('/todos/<id>',methods =['GET'])
def post_details(id):
    todo = Todos.query.get(id)
    return todo_schema.jsonify(todo)

# @desc      Create single todo
# @rout      POST /todos/<id>
# @access    Public
@app.route('/todos',methods=['POST'])
def add_todo():
    title = request.json['title']
    body = request.json['body']

    todos = Todos(title,body)
    db.session.add(todos)
    db.session.commit()
    return todo_schema.jsonify(todos)

# @desc      Update single todo
# @rout      PUT /todos/<id>
# @access    Public
@app.route('/todos/<id>',methods = ['PUT'])
def update_todo(id):
    todo = Todos.query.get(id)

    title = request.json['title']
    body = request.json['body']

    todo.title = title
    todo.body = body

    db.session.commit()
    return todo_schema.jsonify(todo)

# @desc      Delete single todo
# @rout      DELETE /todos/<id>
# @access    Public
@app.route('/todos/<id>',methods=['DELETE'])
def delete_todo(id):
    todo = Todos.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return todo_schema.jsonify(todo)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
