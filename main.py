from gerar_senha import gerar_senha
from flask import Flask, render_template

app = Flask(__name__)

from routes import *

if '__main__' == __name__:
    app.run()
