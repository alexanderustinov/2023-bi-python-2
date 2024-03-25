from flask import Flask, render_template, request

app = Flask(__name__)

def even_numbers(n):
    s = ''
    for i in range(0, n*2, 2):
        s += str(i) + ' '
    return s

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        res = even_numbers(n)
        return render_template('index.html', s=res)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
