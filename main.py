from flask import Flask, redirect
from flask import render_template
from flask import request
import random

app = Flask(__name__)

username = []
usernumbers = []
randomNumber = 0
WinnerName = 'none'
UserNumber_Index = 'none'

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        #getting username from front end
        username.append(request.form['username'])
        # number from front end for every user
        usernumbers.append(int(request.form['number']))
        #generating random number (lottery number) to display in front end 
        
        #logic to select winner by selecting the user whose fav number equals to generated lottery number
        # redirecting to different API
        if len(usernumbers)%5 == 0:
            return redirect('/submit')
            
    return render_template('index.html',User=username,UserNumber=usernumbers,VisitorNumber=len(usernumbers))


@app.route('/submit', methods =['GET'])
def submit():
    randomNumber = random.randint(1,5)
    if randomNumber in usernumbers:
        UserNumber_Index = usernumbers.index(randomNumber)
        print('The winner is ',username[UserNumber_Index])
        print(randomNumber)
        WinnerName = username[UserNumber_Index]
        randomNumber = 0
    return('Winner is '+ WinnerName)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
