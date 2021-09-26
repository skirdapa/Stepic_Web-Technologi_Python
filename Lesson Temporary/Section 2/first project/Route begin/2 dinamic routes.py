from flask import Flask

app = Flask(__name__)


@app.route('/next_number/<int:n>/')
def next_number(n):
    return str(n+1)


@app.route('/')
@app.route('/index/')
def index():
    return 'index'


@app.route('/contact/')
def contact():
    return 'contact information'


@app.route('/calculate/<int:x>/<int:y>/')
def calculate(x, y):
    return str(x**y)


@app.route('/albums/<album_number>/<song_number>/')
def songs(album_number, song_number):
    return f"Это альбом №{album_number} и песня номер {song_number}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
