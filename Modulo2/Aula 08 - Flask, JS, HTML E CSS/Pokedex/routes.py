from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)


@routes.route("/", methods=('GET', 'POST'))
def index():
    pokemons = [
        {
            'numero': '001',
            'nome': 'Bulbasaur'
        },
        {
            'numero': '002',
            'nome': 'Ivysaur'
        },
        {
            'numero': '003',
            'nome': 'Venusaur'
        },
        {
            'numero': '004',
            'nome': 'Charmander'
        },
        {
            'numero': '005',
            'nome': 'Charmeleon'
        },
        {
            'numero': '006',
            'nome': 'Charizard'
        },
    ]
    caminho_base = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'
    return render_template('index.html', pokemons=pokemons, caminho_base=caminho_base)
