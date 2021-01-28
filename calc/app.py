from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum = a + b

    return str(sum)