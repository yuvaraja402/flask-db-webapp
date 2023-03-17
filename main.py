from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

username = []

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        username.append(request.form['name'])
        sorted = set(username)
    return render_template('index.html',username=username)

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)