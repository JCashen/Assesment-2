from flask import Flask, render_template, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/rating', methods=['GET'])
def rating():
    attack = requests.get("http://service-2:5001/atack")
    defence = requests.post("http://service-3:5002/defence")
    rating = (attack*defence)
    return Response(rating, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)