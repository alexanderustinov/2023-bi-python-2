from datetime import datetime

from flask import Flask, render_template

app = Flask("some")

@app.route("/")
def index():
    bread_kinds = ['круассаны', "пончики", "с корицей", "с маком"]
    return render_template('index.html', bread_kinds=bread_kinds, now=datetime.now())

@app.route("/other_page")
def other():
    return render_template('other.html', number=42)