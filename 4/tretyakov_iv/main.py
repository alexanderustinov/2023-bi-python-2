from flask import Flask, render_template, request

app = Flask(__name__)

def gen(n):
    s = ''
    for i in range(n):
        s += str(i+1)+' '
    return s


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        N = int(request.form['N'])
        seq = gen(N)
        su = sum(range(N+1))
        return render_template('index.html', seq=seq, su=su)
    return render_template('index.html', seq='')

