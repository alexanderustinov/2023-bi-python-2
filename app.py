from flask import Flask, render_template, request

app = Flask(__name__)

def bi(n, k):
    if k == 0 or k == n:
        return 1
    return bi(n-1, k-1) + bi(n-1, k)

def f(a):
    list = []
    for a in range(a):
        b = [str(bi(a, k)) for k in range(a+1)]
        list.append(' '.join(b))
    return list

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        list = f(n)
        return render_template('common.html', list=list,)
    else:
        return render_template('common.html')