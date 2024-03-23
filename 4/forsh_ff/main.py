from flask import Flask, render_template
from flask import request


app = Flask(__name__)


def lucas_numbers(n):
    res = [2, 1]
    if n == 0 or n == 1:
        return res
    else:
        for _ in range(n - 1):
            res.append(res[-1] + res[-2])
        return res


@app.route("/")
def index():
    return render_template('page.html')


@app.route("/show_numbers", methods=['POST'])
def show_numbers():
    if request.method == 'POST':
        number = request.form.get('numbers')
        try:
            return render_template('page.html', numbers=lucas_numbers(int(number)))
        except ValueError:
            return render_template('page.html', warning='Enter only integer digits!')
    else:
        return render_template('page.html')


if __name__ == '__main__':
    app.run()
