from pickle import FALSE
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/get', methods = ['GET'])
def hello():
    return jsonify({'hello': 'world'})

@app.route('/pred', methods = ['POST'])
def pred():
    body = request.json['body']
    test_data = request.json
    s1 = json.dumps(test_data)
    print_json = json.loads(s1)
    list = print_json['body']
    input_data = (float(list['age']), float(list['sex']), float(list['chestPainType']),	float(list['restingBP']), float(list['cholestrol']), float(list['fastingBloodSugar']), float(list['restingECG']), float(list['maxHeartRate']), float(list['exerciseAngina']),	float(list['oldpeak']), float(list['STslope']))
    print(input_data)
    return jsonify({'predResult':'1'})


if __name__ == "__main__":
    app.run(debug = False, host = '0.0.0.0')