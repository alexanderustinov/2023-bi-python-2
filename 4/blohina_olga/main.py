from flask import Flask, render_template, request

app = Flask(__name__)

def Factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        sequence = Factorial(n)
        return render_template('index.html', sequence = sequence)
    return render_template('index.html', sequence = '')

app.run(debug = True)

