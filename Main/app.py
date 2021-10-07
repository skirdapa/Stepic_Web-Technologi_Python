import flask
from flask import Flask, render_template, request, Response

from Main.config import Config
from Main.project.forms import MessageForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/", methods=['get', 'post'])
def index():
    server_message = ''
    client_message = ''
    if request.method == 'POST':
        client_message = request.form.get('message')

    if client_message == 'hi':
        server_message = 'Hello!'
    elif client_message != '':
        server_message = "How are you?"
    else:
        server_message = 'Enter your message:'

    return render_template('index.html', message=server_message)


page_news = {'first news': "test text"}


@app.route("/news", methods=['get', 'post'])
def news():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            page_news[title] = content
            return render_template("news.html", news=page_news)
        else:
            return flask.abort(404, 'Неверные параметры запроса - пустые title и/или content')
    return render_template("news.html", news=page_news)


@app.route("/message", methods=['get', 'post'])
def message():
    message_form = MessageForm()
    return render_template("message.html", form=message_form)


@app.route('/old/')
def old_index():
    return render_template('old_index.html')


@app.route('/old/<float:x>/')
def double_x(x):
    y = x*2
    text = f"Ваше число {x}, умноженное на 2:"
    return render_template('old_index.html', text=text, number=y)


# @app.route('/<a>/<b>/<c>')
# def middle(a, b, c):
#     return render_template('index.html', a=a, b=b, c=c)


@app.route('/old/<float:a>/<operator>/<float:c>/')
def calculate(a, operator, c):
    return render_template('old_index.html', a=a, operator=operator, c=c)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

