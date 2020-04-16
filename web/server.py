from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/informacion')
def saludar():
    return "INFORMACION"


@app.route('/esprimo/<numero>')
def es_primo(numero):
    n = int(numero)
    for i in range(2, n):
        if int(numero) % i == 0:
            return False
    return True
@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
