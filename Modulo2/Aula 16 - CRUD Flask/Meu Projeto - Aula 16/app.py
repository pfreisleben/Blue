from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configurações do banco de dados
user = 'dwxnfeeu'  # Usuário do banco
database = 'dwxnfeeu'  # Nome do banco
host = 'tuffi.db.elephantsql.com'  # Host do banco
password = 'EYsro5jAqVKp9hnoUgX_G8Tw3IjMd9Jo'  # Senha do banco

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "chaveOK"

# Cria o objeto SQL Alchemy, passando o app como parametro e vinculando a variavel db.
db = SQLAlchemy(app)

# Modelar em uma classe, a tabela do banco.


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

    @staticmethod
    def read_single(id_registro):
        return Filmes.query.get(id_registro)

    def save(self):
        db.session.add(self)
        db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/read')
def read():
    filmes = Filmes.read_all()
    return render_template('filmes.html', filmes=filmes)


@app.route('/read/<id_registro>')
def filme(id_registro):
    filme = Filmes.read_single(id_registro)
    return render_template('filme.html', filme=filme)


@app.route('/create', methods=('GET', 'POST'))
def create():
    id_atribuido = None
    if request.method == 'POST':
        form = request.form
        print(form)
        registro = Filmes(form['nome'], form['imagem_url'])
        registro.save()
        id_atribuido = registro.id
    return render_template('create.html', id_atribuido=id_atribuido)


if __name__ == '__main__':
    app.run(debug=True)
