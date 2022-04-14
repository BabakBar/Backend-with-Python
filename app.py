from flask import Flask

app = Flask(__name__)

@app.route('/') #decorator - homepage
def index():    #method - response to request
    return 'Hello from Sia!'

app.run(port=5000)