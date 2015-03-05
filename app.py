import os

import bottle
from bottle import route, run, template


@route('/')
def index():
    return 'hello'


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == '__main__':
    run(host='localhost', port=os.environ.get('PORT') or 8080)

app = bottle.default_app()
