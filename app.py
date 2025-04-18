from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except (TypeError, ValueError):
        return jsonify({"error": "Nieprawidłowe dane wejściowe"}), 400
        
    prediction = 1 if (num1 + num2) > 5.8 else 0
    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run()
