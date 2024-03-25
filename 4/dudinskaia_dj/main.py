from flask import Flask, redirect
from sympy import prime

app = Flask(__name__)

def generate_primes(n):
    return [prime(i) for i in range(1, n+1)]

@app.route('/')
def redirect_primes():
    return redirect('/primes/42')


@app.route('/primes/<int:n>')
def show_primes(n):
    primes = generate_primes(n)
    return f"The first {n} prime numbers are: {primes}<br><br>(just use the address bar)"

if __name__ == '__main__':
    app.run(debug=True)
