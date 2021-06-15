from flask import Blueprint, render_template

bp = Blueprint('bp', __name__)


@bp.route("/")
def hello_world():
    return"<h1>Hello World!!</h1>"


@bp.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Olá, "+nome+"<br/> Faca seu login!</h1></center>"


@bp.route("/auladeontem/")
def carrega():
    return render_template("inicio.html")
