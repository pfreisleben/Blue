import random
from flask import Flask, Blueprint, render_template
bp = Blueprint('bp', __name__)


@bp.route("/")
def index():
    nome = "Betão Einstein"
    idade = 42
    imagemSerio = "https://wallsdesk.com/wp-content/uploads/2017/01/Albert-Einstein-Wallpapers-HD.jpg"
    imagemLocao = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fih1.redbubble.net%2Fimage.284215355.6088%2Fflat%2C750x1000%2C075%2Ct.u5.jpg&f=1&nofb=1"
    chance = random.randint(1, 2)
    if chance == 1:
        imagem = imagemSerio
        mensagem = "Betão tá sério!"
    else:
        imagem = imagemLocao
        mensagem = "Betão tá locão!"
    return render_template('index.html', nome=nome, idade=idade, imagem=imagem, mensagem=mensagem
                           )
