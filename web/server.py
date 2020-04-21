from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/static/html/cs_utec')
def cs_utec():
    return "cs_utec"


@app.route('/static/html/cs2b01')
def cs2b01():
    return "cs2b01"


@app.route('/static/html/informacion')
def informacion():
    return "INFORMACION"


@app.route('/esprimo/<numero>')
def es_primo(numero):
    n = int(numero)
    for i in range(2, n):
        if int(numero) % i == 0:
            return str(False)
    return str(True)


@app.route('/palindrome/<palabra>')
def palindrome(palabra):
    pal2 = palabra.lower()
    reversa = ""
    for i in range(len(pal2)):
        x = len(palabra) - i - 1
        reversa = reversa + pal2[x]
    if reversa == pal2:
        return str(True)
    else:
        return str(False)


@app.route('/multiplo/<numero1>/<numero2>')
def es_multiplo(numero1,numero2):
    if int(numero1) % int(numero2) == 0:
        return str(True)
    return str(False)


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
