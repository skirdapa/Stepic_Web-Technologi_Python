from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return 'index'


@app.route('/contact/')
def contact():
    return 'contact information'


@app.route('/calculate/7/9/')
def calculate():
    return str(7**9)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
