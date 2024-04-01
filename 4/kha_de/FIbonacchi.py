from flask import Flask, render_template, request

app = Flask(__name__)

def Fibbonacci(n):
    if n == 1:
        s = '1'
    elif n == 2:
        s = '1, 1'
    else:
        a, b = 1, 1
        s = '1, 1'
        while n > 2:
            a, b = b, a + b
            s += ', ' + str(b)
            n -= 1
    return s

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        sequence = Fibbonacci(n)
        return render_template('index.html', sequence = sequence)
    return render_template('index.html', sequence = '')

app.run(debug = True)