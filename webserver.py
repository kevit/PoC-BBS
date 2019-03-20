from flask import Flask, jsonify
from flask import request
from flask import abort
import random
import string
import docker

import logging

handler = logging.StreamHandler()
root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(handler)

app = Flask(__name__)

ports = ['4200','4201','4202']
@app.route('/', methods=['GET','PUT'])
def notimp():
    abort(501)

@app.route('/', methods=['POST'])

def post():
    if len(ports) == 0:
        return 'no more', 429
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p =  "".join(random.sample(s,8))
    b = ports.pop()
    client = docker.from_env()
    container = client.containers.run("sspreitzer/shellinabox", environment=dict([("SIAB_PASSWORD", p)]),ports=dict([("4200/tcp", b)]), detach=True)
    

    return 'password: ' + p + '  port:' + b, 201

@app.route('/', methods=['DELETE'])
def delete():
    client = docker.from_env()
    for container in client.containers.list():
      container.stop()
    return 'deleted', 201
      
if __name__ == '__main__':
    app.run(debug=True)
