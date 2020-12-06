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

    if level == "level 1" and affluence == "ice":
        name = "Jeanne"
    elif  level == "level 2" and affluence == "ice":
        name = "Orla"
    elif  level == "level 3" and affluence == "ice":
        name = "Reuben"
    elif  level == "level 4" and affluence == "ice":
        name = "Ferguson"
    elif  level == "level 5" and affluence == "ice":
        name = "Perookie"
    
    elif  level == "level 1" and affluence == "dark":
        name = "Helllins"
    elif  level == "level 2" and affluence == "dark":
        name = "Allenula"
    elif  level == "level 3" and affluence == "dark":
        name = "Has"
    elif  level == "level 4" and affluence == "dark":
        name = "Lollivan"
    elif  level == "level 5" and affluence == "dark":
        name = "Cootha"

    elif  level == "level 1" and affluence == "light":
        name = "Abanes"
    elif  level == "level 2" and affluence == "light":
        name = "Visermas"
    elif  level == "level 3" and affluence == "light":
        name = "Jostompa"
    elif  level == "level 4" and affluence == "light":
        name = "Arimar"
    else:
        name = "Murell"


    return Response(name, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)