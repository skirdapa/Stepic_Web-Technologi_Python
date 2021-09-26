from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<float:x>/')
def double_x(x):
    y = x*2
    text = f"Ваше число {x}, умноженное на 2:"
    return render_template('index.html', text=text, number=y)


# @app.route('/<a>/<b>/<c>')
# def middle(a, b, c):
#     return render_template('index.html', a=a, b=b, c=c)


@app.route('/<float:a>/<operator>/<float:c>/')
def calculate(a, operator, c):
    return render_template('index.html', a=a, operator=operator, c=c)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

