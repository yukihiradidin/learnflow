from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "status": {
            "code" : 200,
            "message" : "success fetching api"
        },
        "data": None
    }), 200

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Handle the POST request 
        data = request.get_json()
        if data is not None:
            #prediction = perform_prediction(data)
            
            return jsonify({
                "status": {
                    "code": 200,
                    "message": "success"
                },
                "data": None
            }), 200
        else:
            return jsonify({
                "status": {
                    "code": 405,
                    "message": "Bad Request - Data must be in JSON format"
                },
                "data": None
            }), 405

    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "method not allowed"
            },
            "data": None
        }), 405

if __name__=="__main__":
    app.run()
