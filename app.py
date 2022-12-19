from flask import Flask 
from flask import  request
import joblib

app = Flask(__name__)

filename = './knn_polution_density_model.sav'

proximity_model = joblib.load(filename)

@app.route('/proximity', methods=['GET'])
def hello():
    args = request.args
    print(args)
    proximity_city = proximity_model.predict([[float(args.get('pollution')), float(args.get('airCo'))]])
    
    return str(proximity_city[0])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)