from flask import Flask, redirect
import math

app = Flask(__name__)

def Factorial(n):
    for i in range(1, n+1):
        return [math.factorial(i) for i in range(1, n+1)]

@app.route('/')
def Redirect_Fact():
    return redirect('/fact/4')


@app.route('/fact/<int:n>')
def Your_Factorials(n):
    fact = Factorial(n)
    return f'Вот первые {n} члена(ов) факториальной последовательности: {fact}'

if __name__ == '__main__':
    app.run(debug=True)
