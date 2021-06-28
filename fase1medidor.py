from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/fase1.html')
def fase1():
    fase = 1
    
    return render_template('fase1.html',fase=fase)
