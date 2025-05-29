from flask import Flask, render_template, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

AUTH = HTTPBasicAuth('wsfarmina_zendesk', 'test')
BASE_URL_PRODUCTS = "https://gw-c.petgenius.info/wfservice/z1/nutritionalplans/products/list"
BASE_URL_CARES = "https://gw-c.petgenius.info/wfservice/z1/specialcares/list"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/specialcares", methods=["POST"])
def get_specialcares():
    species = request.json.get("species", "dog")
    payload = {
        "species": species,
        "country": "MA",
        "languageId": "1",
        "type": "dietetic"
    }
    res = requests.post(BASE_URL_CARES, json=payload, auth=AUTH)
    return jsonify(res.json())

@app.route("/products", methods=["POST"])
def get_products():
    filters = request.json
    payload = {
        "country": "MA",
        "languageId": "20",
        "productType": filters.get("productType"),
        "type": filters.get("type"),
        "lifeStage": filters.get("lifeStage"),
        "gestation": filters.get("gestation") == True,
        "lactation": filters.get("lactation") == True,
        "specialcares": filters.get("specialcares", []),
        "appsAndEshop": True
    }
    res = requests.post(BASE_URL_PRODUCTS, json=payload, auth=AUTH)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(debug=True)
