from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def get_location_names():
    




if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    app.run()