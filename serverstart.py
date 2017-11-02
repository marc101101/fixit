from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

from helper.InvalidUsage import InvalidUsage
from helper.GetBestPrice import GetBestPrice

app = Flask(__name__)
CORS(app)

"""
POST /getRepairPrice/
"""

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# GET /getRepairPrice/

@app.route("/getRepairPrice/", methods=['POST'])
def get_repair_price():
    try:
        if request.method == 'POST':
            popular_tags_obj = GetBestPrice()
            return popular_tags_obj.getPrice(request.headers['brand'],
                                             request.headers['model'],
                                             request.headers['damaged'],
                                             request.headers['long_response'])

    except Exception as e:
        print(e)
        raise InvalidUsage('Not Found', status_code=404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
