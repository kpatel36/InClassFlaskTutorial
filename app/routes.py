# flask routes control what content is shown on what url depending on how the user is accessing that url, what button they've pressed, etc
# the general structure of a flask route is a function with a decorator
# a decorator adds lines of code that run before and after the decorated function

# our first route:
# goal display the index.html when use navigates to the base url aka 'http://127.0.0.1:5000/'

# in order to do this we need a few tools
# 1. we need access to our app
from app import app # import the app variable defined in __init__.py
# 2. we need the ability to show an html file at a specified url
from flask import render_template 
    # render_template lets us pass in the name of an html file from our templates folder for the routes to display
    # if your route's job is to display an html page, return value should be a call to render_template

@app.route('/') # decorator says 'this function is a route of the flask app 'app' with the url endpoint'/''
def home():
    #these are normal python functions - we can write whatever python coding we want within these python functions
    print ('Hello Foxes!')
    x = choice(['Seth', 'Ryan','Marissa,', 'Summer'])
    print (f'X has value{x}. this will print in the terminal when this function runs when the url endpoint / is accessed')
    return render_template('index.html')
# aka configure our flask app from our Config object we just wrote


@app.route('/mcfc')
def mancity():
    headline = "Manchester City beat Sporting Lisbon in the Champions League Round of 16!"
    mcgoals = 5
    sportinggoals = 4
    return render_template('soccer.html',headline=headline, mcfg=mcgoals, slg=sportinggoals)