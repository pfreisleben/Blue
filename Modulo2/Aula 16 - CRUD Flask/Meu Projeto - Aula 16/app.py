from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configurações do banco de dados
user = 'dwxnfeeu'  # Usuário do banco
database = 'dwxnfeeu'  # Nome do banco
host = 'tuffi.db.elephantsql.com'  # Host do banco
password = 'EYsro5jAqVKp9hnoUgX_G8Tw3IjMd9Jo'  # Senha do banco

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "uma chave secreta bem secreta"

# Cria o objeto SQL Alchemy, passando o app como parametro e vinculando a variavel db.
db = SQLAlchemy(app)


class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url

    @staticmethod
    def read_all():
        return Filmes.query.all()


@app.route('/')
def index():
    return render_template('index.html')
