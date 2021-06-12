from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/calculate')
def calculate():
    return render_template('chart.html')
@app.route('/calculateWR')
def calculateWR():
    return render_template('chart2.html')
if __name__ == '__main__':
    app.run(debug = True)