from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/rating', methods=['GET'])
def rating():
    ratings = ["level 1", "level 2", "level 3", "level 4", "level 5"]
    return Response(random.choices(ratings), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)