from flask import Flask, request, render_template, redirect,url_for
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import os
app = Flask(__name__,static_folder='static', static_url_path='')
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