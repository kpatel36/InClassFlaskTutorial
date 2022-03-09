# set up and organize the applications general config
# what secret variables does it need (secret key, database info, mailer info, api keys, etc.)
# what does it's file structure look like


# we're going to get a little help from the os packages
import os 

# set up the base directory of the entire application - aka help our computer figure out our file system and where to find the different places of this project
basedir = os.path.abspath(os.path.dirname(__name__)) ## this line with two function calls set equal to basedir var...XX

# config variables setup
class Config:
    """
    set configuation variables for our entire flask app
    set names - variables must be the names listed "FLASK_APP" "FLASK_ENV" "SECRET_KEY"
    """

    FLASK_APP = os.environ.get('FLASK_APP') #go get the the FLASK_APP value from .env
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')