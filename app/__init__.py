# imports at the top of any necessary modules/files/classes/packages/functions - whatwever we need from other files for this file to work
# from the flask package that we isntalled, import the flask object/class
from flask import Flask
# from our config file, import the Config class that we created
from config import Config

# define/instantiate our Flask object...aka tell the computer that this is a flask app
# pretty standard to call instantiation variable 'app'. if you change it to something else, youll need to change other elements of code 
# need to tell the app how it should be configured (production dev app, etc) - head over to the config.py file to do this
app = Flask(__name__)

# tell the app how it should be configured - over to the config.py file to set up for this!
app.config.from_object(Config)
# aka configure our flask app from the Config object we just wrote
