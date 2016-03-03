#!/usr/bin/python
def app(environ, start_response):

    data = ''

    d = environ['QUERY_STRING'].split('&')
    for e in d:
	data += e + '\n'

    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [data]
