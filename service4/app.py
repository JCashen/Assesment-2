from flask import Flask, render_template, Response, request
import requests
import random

app = Flask(__name__)

@app.route('/name', methods=['POST'])
def name():
    character = request.data.decode('utf-8')
    data = character.split(",")
    level = data[0]
    affluence = data[1]

    if level == "1 Star" and affluence == "water":
        name = "Jeanne"
    elif  level == "2 Star" and affluence == "water":
        name = "Orla"
    elif  level == "3 Star" and affluence == "water":
        name = "Reuben"
    elif  level == "4 Star" and affluence == "water":
        name = "Ferguson"
    elif  level == "5 Star" and affluence == "water":
        name = "Perookie"
    
    elif  level == "1 Star" and affluence == "fire":
        name = "Helllins"
    elif  level == "2 Star" and affluence == "fire":
        name = "Allenula"
    elif  level == "3 Star" and affluence == "fire":
        name = "Has"
    elif  level == "4 Star" and affluence == "fire":
        name = "Lollivan"
    elif  level == "5 Star" and affluence == "fire":
        name = "Cootha"

    elif  level == "1 Star" and affluence == "lightning":
        name = "Abanes"
    elif  level == "2 Star" and affluence == "lightning":
        name = "Visermas"
    elif  level == "3 Star" and affluence == "lightning":
        name = "Jostompa"
    elif  level == "4 Star" and affluence == "lightning":
        name = "Arimar"
    else:
        name = "Murell"


    return Response(name, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)