from flask import Flask, Blueprint, render_template
bp = Blueprint('bp', __name__)


@bp.route("/")
def index():
    nome = "Marcio"
    idade = 17
    cidade = "São Paulo"
    imagem = "/static/logo-blue-croped.gif"
    if idade >= 18:
        maiordeidade = True
    else:
        maiordeidade = False
    return render_template('index.html', nome=nome, idade=idade, cidade=cidade, imagem=imagem, maiordeidade=maiordeidade
                           )
