from flask import Flask, render_template, Response, request 
import requests
import random

app = Flask(__name__)

@app.route('/defence', methods=['GET'])
def defence():
    return Response(random.randint(1, 5), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)