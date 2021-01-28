"""Give four routes for performing the basic four math operations"""

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """Return a string of a + b"""

    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(add(a, b))

@app.route('/sub')
def subtract_nums():
    """Return a string of a - b"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(sub(a, b))

@app.route('/mult')
def multiply_nums():
    """Return a string of a * b"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(mult(a, b))

@app.route('/div')
def divide_nums():
    """Return a string of a / b"""

    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(div(a, b))