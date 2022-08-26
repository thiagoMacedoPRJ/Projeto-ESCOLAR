from flask import Flask, request, render_template, redirect, jsonify 
from random import *
import os


app = Flask(__name__)
app.secret_key = 'biosec'



# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')


def main():
    p = randint(0, 500000)
    port = int(os.environ.get("PORT", p))
    app.run(host="0.0.0.0", port= port)
    

if __name__ == '__main__':
    main()
