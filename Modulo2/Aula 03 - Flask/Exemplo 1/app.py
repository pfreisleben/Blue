from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return"<h1>Hello World!!</h1>"


@app.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>Olá, "+nome+"<br/> Faca seu login!</h1></center>"


@app.route("/auladeontem/")
def carrega():
    return render_template("inicio.html")


if(__name__ == "__main__"):
    app.run(debug=True)
