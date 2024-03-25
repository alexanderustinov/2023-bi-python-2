from flask import Flask, render_template, request

app = Flask(__name__)

def padovan_numbers(n):
    first_numbers = [1, 1, 1]
    if n == 0 or n == 1 or n == 2:
        return first_numbers
    else:
        for i in range(n-1):
            first_numbers.append(first_numbers[-2] + first_numbers[-3])
        return first_numbers

@app.route("/")
def index():
    return render_template('page.html')

@app.route("/show", methods=['POST'])
def show():
    if request.method == 'POST':
        number = request.form.get('numbers')
        try:
            return render_template('page.html', numbers=padovan_numbers(int(number)))
        except ValueError:
            return render_template('page.html', warning='Enter only integer numbers and nothing else!')
    else:
        return render_template('page.html')

if __name__ == '__main__':
    app.run()
