from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    
    return render_template('index.html',columny = 8, rowx= 8, colorone = 'red', colortwo = 'black',)

@app.route('/<int:num>')
def column(num):
    return render_template('index.html',columny = num, rowx= 8, colorone = 'red', colortwo = 'black',)

@app.route('/<int:numy>/<int:numx>')
def columnrow(numy,numx):
    return render_template('index.html', columny = numy, rowx= numx, colorone = 'red', colortwo = 'black',)

@app.route('/<int:numy>/<int:numx>/<coloroneR>')
def columnrowcolorone(numy,numx,coloroneR):
    return render_template('index.html', columny = numy, rowx= numx, colorone = coloroneR, colortwo = 'black',)

@app.route('/<int:numy>/<int:numx>/<coloroneR>/<colortwoR>')
def columnrowcoloronetwo(numy,numx,coloroneR,colortwoR):
    return render_template('index.html', columny = numy, rowx= numx, colorone = coloroneR, colortwo = colortwoR,)
if __name__ == "__main__":
    app.run(debug=True)
