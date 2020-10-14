import os
from flask import Flask, jsonify, request
from math import sqrt


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    nmax = 100

    n1 = 0
    n2 = 1
    cont = 0
    fib = 0

    fib = ("Esses são os 1000 primeiros numeros da razão Fibonacci: <br> <br>")

    while cont < nmax:
        fib = n1 + n2
        n1 = n2
        n2 = fib
        cont = cont + 1
    return fib

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
