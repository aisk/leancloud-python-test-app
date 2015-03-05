import os

from bottle import route, run, template


@route('/')
def index():
    return 'hello'


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=os.environ.get('PORT') or 8080)
