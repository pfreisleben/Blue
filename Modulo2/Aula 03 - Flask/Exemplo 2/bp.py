from flask import Flask, Blueprint, render_template
bp = Blueprint('bp', __name__)


@bp.route("/")
def index():
    nome = "Marcio"
    idade = 25
    cidade = "São Paulo"
    imagem = "/static/logo-blue-croped.gif"
    return render_template('index.html', nome=nome, idade=idade, cidade=cidade, imagem=imagem)
