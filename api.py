from flask import Flask, jsonify, Response, json, request
from custom_modules.api_functions import get_car_by_plate, get_random_cars_brand

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Welkom </h1>"


@app.route("/show_car/<kenteken>", methods=['GET'])
def show_car(kenteken):
    car = get_car_by_plate(kenteken)
    if car == None:
        message_dict = {"Melding": "😔 Dit kenteken is niet gevonden"}
        return jsonify(message_dict)
    return jsonify(car)


@app.route("/random_cars_brand", methods=['POST'])
def random_cars_brand():
    brand = request.args.get('brand')
    color = request.args.get('color')
    cars_list = get_random_cars_brand(brand, color)
    cars_json = json.dumps(cars_list)
    return Response(cars_json,
                    mimetype="application/json",
                    )


if __name__ == '__main__':
    app.run()