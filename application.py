from flask import Flask, Response, request
import json

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get_root():
    return Response(json.dumps({'Output': 'Hello Get World'}), mimetype='application/json', status=200)
    

@application.route('/', methods=['POST'])
def post_root():
    return Response(json.dumps({'Output': 'Hello Post World'}), mimetype='application/json', status=200)


@application.route('/calc/currency/<string:currency>', methods=['POST'])
def post_currency(currency):
    res = currency_rate.get(currency, 0.00) 
    return Response(json.dumps({currency: res}), mimetype='application/json', status=200)


currency_rate = {
    'usd' : 3.3,
    'pound' : 4.5
}


if __name__ == "__main__":
    application.debug = True
    application.run()