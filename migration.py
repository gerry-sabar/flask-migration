from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# tidak bisa running migration dari sini hanya bisa declare class langsung
# from models.log import Log

# bagian ini di uncomment jalan generate migration baru
#class Log(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    detail = db.Column(db.Text)

if __name__ == '__main__':
    manager.run()
