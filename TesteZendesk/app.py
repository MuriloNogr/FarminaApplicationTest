from flask import Flask, render_template, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

FARMINA_AUTH = HTTPBasicAuth('wsfarmina_zendesk', 'test')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/specialcares', methods=['POST'])
def get_specialcares():
    data = request.json
    payload = {
        "species": data.get("species", "dog"),
        "country": "MA",
        "languageId": "1",
        "type": "dietetic"
    }

    response = requests.post(
        "https://gw-c.petgenius.info/wfservice/z1/specialcares/list",
        auth=FARMINA_AUTH,
        json=payload
    )

    if response.status_code == 200:
        try:
            result = response.json()
            cares = result["result"][0]["specialcares"][0]["list"]
            return jsonify(cares)
        except Exception:
            return jsonify([]), 200
    return jsonify([]), 200

@app.route('/products', methods=['POST'])
def get_products():
    data = request.json

    payload = {
        "country": "MA",
        "languageId": "20",
        "productType": data.get("productType", "dry"),
        "type": data.get("type"),
        "lifeStage": data.get("lifeStage"),
        "gestation": data.get("gestation"),
        "lactation": data.get("lactation"),
        "specialcares": data.get("specialcares"),
        "appsAndEshop": True
    }

    response = requests.post(
        "https://gw-c.petgenius.info/wfservice/z1/nutritionalplans/products/list",
        auth=FARMINA_AUTH,
        json=payload
    )

    try:
        return jsonify(response.json())
    except Exception:
        return jsonify({"status": 500, "message": "Error parsing response"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
