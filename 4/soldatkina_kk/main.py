from flask import Flask, render_template, request

app = Flask(__name__)

def triangular_numbers(n):
    s = ''
    for i in range(0, n + 1):
        s += str(int((i**2+i)/2))
        if i != n:
            s += ', '
    return s

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        res = triangular_numbers(n)
        return render_template('index.html', s=res)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
