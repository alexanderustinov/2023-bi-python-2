from flask import Flask, render_template, request

app = Flask(__name__)

def Factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/show_factorials', methods=['POST'])
def show_factorials():
    if request.method == 'POST':
        factorial = request.form.get('factorials')
        try:
            return render_template('page.html', factorials=Factorial(int(factorial)))
        except ValueError:
            return render_template('page.html', error='Пожалуйста, введите натуральное число.')
    else:
        return render_template('page.html')

if __name__ == '__main__':
    app.run()
