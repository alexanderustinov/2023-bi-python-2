from flask import Flask
from sympy import prime

app = Flask(__name__)

def generate_primes(n):
    return [prime(i) for i in range(1, n+1)]

@app.route('/primes/<int:n>')
def show_primes(n):
    primes = generate_primes(n)
    return f"The first {n} prime numbers are: {primes}"

if __name__ == '__main__':
    app.run(debug=True)