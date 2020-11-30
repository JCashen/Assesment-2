from flask import Flask, render_template 
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    #gets an attack rating
    attack = requests.get("http://service-2:5001/atack")
    #gets defence rating
    defence = requests.post("http://service-3:5002/defence")
    #gets overall rating
    rating = requests.get("http://service-4:5003/rating")


    return render_template('index.html', attack=attack.text, defence=defence.text, rating=rating.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')