from flask import Flask, jsonify, request
import pygeohash as gh

app = Flask(__name__)


@app.route("/saludo")
def hello():
    return jsonify({'response': 'hola mundo'})

@app.route('/geo', methods=['GET'])
def geo():
    try:
        latitud = float(request.args['lat'])
        longitud = float(request.args['long'])
        geohash = gh.encode(latitud, longitud, precision=12)
    except:
        print("Se presento un error") 

    return jsonify({'latitud': latitud,
                    'longitud': longitud,
                    'geohash': geohash
                    })  

def suma(num1,num2):
    return num1+num2   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)