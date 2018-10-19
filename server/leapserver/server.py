#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

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

def start():
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
        try:
            es = decode(e.output).split("\r\n")
            # r = dict(error='Exception', output=decode(e.output))

            p1 = r"line\s\d+"
            pattern1 = re.compile(p1)
            matcher1 = re.search(pattern1, es[1])

            line = matcher1.group(0)
            r = dict(error='Exception', output=es[-2] + " (" + line + ")")
        except:
            r = dict(error='Exception', output=decode(e.output))

    print('Execute done.')

    return [json.dumps(r).encode('utf-8')]

start()
