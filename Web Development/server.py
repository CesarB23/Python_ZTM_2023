#How to run flask application:
    #flask --app 'file name' run
#Run application in debugger mode:
    #flask --app 'file-name run --debug
from flask import Flask, render_template
app = Flask(__name__)
# print(__name__)
# print(app)

@app.route('/')
def hello_world():
    return 'POPO'

@app.route('/blog')
def blog():
    return 'Blog'

@app.route('/blog/2020/dogs')
def blog2():
    return 'Dogs 2020'

#Sending HTML Template to the server
@app.route('/index.html')
def index():
    return render_template('index.html')