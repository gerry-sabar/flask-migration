from main import db


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.Text)
