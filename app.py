# coding: utf-8

import sys


def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'

    print 'xxx'

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(output)))
    ]
    start_response(status, response_headers)

    return [output, str(sys.stdout)]
