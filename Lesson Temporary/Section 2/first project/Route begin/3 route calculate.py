from flask import Flask

app = Flask(__name__)


def calculate(x, operator, y):
    if operator == ":":
        return str(x/y)
    else:
        s = str(x) + str(operator) + str(y)
        return str(eval(s))


@app.route('/<int:x><operator><int:y>/')
def operations(x, operator, y):
    return calculate(x, operator, y)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
