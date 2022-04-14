from flask import Flask

app = Flask(__name__)

@app.route('/') #decorator - homepage
def index():
    return 'Hello from Docker!'