#!/usr/bin/python3
"script displays 5 routes"

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_function():
    "Return some text"
    return 'Hello HBNB!'

@app.route('/hbnb')
def texter():
    "return text"
    return 'HBNB'

@app.route('/c/<text>')
def c_text(text):
    "takes text as a parameter and return it"
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/<text>')
def python_text(text):
    "takes text as a parameter and return it"
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<n>')
def integer_num(n):
    "function return a number if it is integer only"
    if isinstance(n, int)
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
