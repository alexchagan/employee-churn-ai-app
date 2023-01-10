from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/api/", methods=['POST', 'GET'])
def get_answers():
    if request.method == 'POST':
        print('post app')
        req = request.json
        print(req)
        return jsonify(name='john')

if __name__ == "__main__":
    app.run(debug=True)