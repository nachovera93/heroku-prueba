from flask import Flask, render_template
import fase1medidor

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

#@app.route('/fase1.html')
#def fase1():
 #     return render_template('fase1.html')



if __name__ == '__main__': 
     app.run(debug=False)