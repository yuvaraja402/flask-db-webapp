from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

username = []

@app.route('/', methods =["GET", "POST"])
def homepage():
    if request.method == 'POST':
        username.append(request.form['name'])
        sorted = set(username)
    return render_template('page.html',username=username,sorted=sorted)


if __name__ == "__main__":
    app.run(host="localhost", port=8004,debug=True)