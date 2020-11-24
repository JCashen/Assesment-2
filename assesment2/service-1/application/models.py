from application import db 

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attack = db.Column(db.Integer)
    defence = db.Column(db.Integer)
    power_level = db.Column(db.Integer)