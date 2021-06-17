from flask import Blueprint, render_template

bp = Blueprint('bp', __name__)


@bp.route("/")
def index():
    personagens = [{'nome': 'globin'}, {'nome': 'orc'}, {'nome': 'feiticeira'}]
    armas = [{'nome': 'arco'}, {'nome': 'espada'}, {'nome': 'soco'}]
    return render_template('index.html', personagens=personagens, armas=armas)
