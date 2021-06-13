from flask import Flask, request, render_template, redirect,url_for
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import os
app = Flask(__name__,static_folder='static', static_url_path='')
#Details of azure account
app.config.from_pyfile('config.py')
account = app.config['ACCOUNT_NAME']   # Azure account name
key = app.config['ACCOUNT_KEY']      # Azure Storage account access key  
connect_str = app.config['CONNECTION_STRING']
container = app.config['CONTAINER'] # Container name
allowed_ext = app.config['ALLOWED_EXTENSIONS'] # List of accepted extensions

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allowed_ext

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