from flask import Flask, render_template 
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from models import gacha

pw = getenv('MYSQL_ROOT_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:' + pw + '@database:3306/database'
db = SQLAlchemy(app)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #gets a rating
    rating = requests.get("http://service2:5001/rating")
    #gets affluence
    affluence = requests.get("http://service3:5002/affluence")
    #gets character name
    character = str(rating.text) + "," + str(affluence.text)
    name = requests.post("http://service4:5003/name", data=character)
    
    gach = gacha(star=str(rating.text), affluence=str(affluence.text) names=str(name.text))
    db.session.add(gach)
    db.session.commit()

    return render_template('index.html', rating=rating.text, affluence=affluence.text, name=name.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')