from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/read')
def read_all():
    return render_template('read_all.html')


if __name__ == '__main__':
    app.run(debug=True)
