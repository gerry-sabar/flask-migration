from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

# later you can use looping file logic as the app is getting bigger & more files are created
from views.web import *
from views.api import *

if __name__ == '__main__':
    app.run()