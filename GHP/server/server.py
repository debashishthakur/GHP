from flask import Flask, request, jsonify
app = Flask(__name__)
import util

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods=['POST', 'GET'])
def predict_home_price():
    if request.method == 'POST':
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        print("location in server", location, bhk, bath, total_sqft)
        response = jsonify({
            'estimated_price' : util.get_estimated_price(location, total_sqft, bhk, bath)
        })
            
        response.headers.add('Access-Cotrol-Allow-Origin', '*')
        return response

if __name__ == "__main__":
    print("Starting Python Flask server ...")
    util.load_saved_artifacts()
    app.debug = True
    app.run()
    app.run(debug=True)