from flask import Flask, render_template 
import requests

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


    return render_template('index.html', rating=rating.text, affluence=affluence.text, name=name.text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')