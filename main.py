from flask import Flask
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

        WinnerName = 'none'

        #getting username from front end
        username.append(request.form['username'])
        # number from front end for every user
        usernumbers.append(int(request.form['number']))
        #generating random number (lottery number) to display in front end 
        
        #logic to select winner by selecting the user whose fav number equals to generated lottery number
        if len(usernumbers)%5 == 0:
            randomNumber = random.randint(1,5)
            if randomNumber in usernumbers:
                UserNumber_Index = usernumbers.index(randomNumber)
                print('The winner is ',username[UserNumber_Index])
                print(randomNumber)
                WinnerName = username[UserNumber_Index]
                randomNumber = 0
     


    return render_template('index.html',User=username,UserNumber=usernumbers,Winner=WinnerName,VisitorNumber=len(usernumbers))


#@app.route('/submit', methods =['GET'])
#def submit():
#    return('hello!')


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)