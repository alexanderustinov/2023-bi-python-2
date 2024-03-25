from math import factorial
from flask import Flask, render_template, request


def catalans(n):
    return int(factorial(2*n)/(factorial(n)*factorial(n+1)))

name = "Catalan's Numbers"
app = Flask(name)
html_file="index.html"
nums = []
@app.route('/', methods=['GET', 'POST'])
def doit():
    N=""
    if request.method == "POST":
        N = int(request.form['number'])
        del nums[:]
        for i in range(N):
            nums.append(catalans(i))
        return render_template(html_file, name=name, nums=nums, N=N)
    return render_template(html_file, name=name)


if name == name:
  app.run(debug=True)