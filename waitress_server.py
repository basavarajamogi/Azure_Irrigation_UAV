import os
from waitress import serve
from irriapp import app
serve(app, host='0.0.0.0', port=8080)