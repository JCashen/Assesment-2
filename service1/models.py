from app import db

class gacha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    star = db.Column(db.String(10), nullable=False)
    affluence = db.Column(db.String(10), nullable=False)
    names = db.Column(db.String(10), nullable=False)