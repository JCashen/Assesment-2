from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/attack', methods=['GET'])
def attack():
    return Response(random.randint(1, 5), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)