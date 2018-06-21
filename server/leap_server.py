#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def check_version():
    v = sys.version_info
    if v.major == 3 and v.minor >= 4:
        return True
    print('Your current python is %d.%d. Please use Python 3.4+' % (v.major, v.minor))
    return False

if not check_version():
    exit(1)

import os, io, json, subprocess, tempfile
from urllib import parse
from wsgiref.simple_server import make_server

# EXEC = sys.executable
EXEC = "python"
PORT = 56978

TEMP = tempfile.mkdtemp(prefix='LeapLearner_')

def main():
    httpd = make_server('127.0.0.1', PORT, application)
    print('Ready for Python code on port %d...' % PORT)
    httpd.serve_forever()


def write_py(name, code):
    fpath = os.path.join(TEMP, '%s.py' % name)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    return fpath

def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')

def application(environ, start_response):

    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO')

    if method != 'POST' or path != '/run' or \
        not environ.get('CONTENT_TYPE', '').lower().startswith('application/x-www-form-urlencoded'):

        start_response('400 Bad Request', [('Content-Type', 'application/json')])
        return [b'{"error":"bad_request"}']

    s = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
    qs = parse.parse_qs(s.decode('utf-8'))

    if not 'code' in qs:
        start_response('400 Bad Request', [('Content-Type', 'application/json')])
        return [b'{"error":"invalid_params"}']

    name = 'temp'
    code = qs['code'][0]

    headers = [('Content-Type', 'application/json')]
    origin = environ.get('HTTP_ORIGIN', '')
    headers.append(('Access-Control-Allow-Origin', origin))
    start_response('200 OK', headers)

    r = dict()

    try:
        fpath = write_py(name, code)
        print('Running')
        r['output'] = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT))
    except subprocess.CalledProcessError as e:
        r = dict(error='Exception', output=decode(e.output))
    except subprocess.CalledProcessError as e:
        r = dict(error='Error', output='执行错误')

    print('Execute done.')

    return [json.dumps(r).encode('utf-8')]

if __name__ == '__main__':
    main()
