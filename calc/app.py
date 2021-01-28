from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(add(a, b))

@app.route('/sub')
def subtract_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a, b))
