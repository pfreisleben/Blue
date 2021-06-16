from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)


@routes.route("/", methods=('GET', 'POST'))
def index():
    nome = None
    sobrenome = None
    return (render_template('index.html'))
