import os


#linking files/folder               #flask thing
basedir = os.path.abspath(os.path.dirname(__file__))

#setup config variable for flask app
class Config:
    """
        setup config vars 4 flask
        ENVIRONMNENTAL VARIABLES
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if os.environ.get('DATABASE_URL').startswith('postgres'):   #the workaround for SQL
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #stoptracking databases changes through sqlalchemy