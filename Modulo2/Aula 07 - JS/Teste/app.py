from flask import Flask  # Importa flask
from routes import routes  # Importa o Blueprint "routes" criado em ./routes.py

app = Flask(__name__)  # Instancia o Flask
app.register_blueprint(routes)

if (__name__ == "__main__"):
    app.run(Debug=True)
