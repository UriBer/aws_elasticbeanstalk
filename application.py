from flask import Flask, Response, request
import requests
import json

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get_root():
    return Response(json.dumps({'Output': 'Hello Get World'}), mimetype='application/json', status=200)
    

@application.route('/', methods=['POST'])
def post_root():
    return Response(json.dumps({'Output': 'Hello Post World'}), mimetype='application/json', status=200)


@application.route('/calc/currency/<string:currency>', methods=['GET'])
def get_currency(currency):
    res = currency_rate.get(currency, 0.00) 
    return Response(json.dumps({currency: res}), mimetype='application/json', status=200)


# get example for multiplication
# test get  
# curl -i http://"localhost:5000/v1/multiply?first_num=12.1&second_num=12"

@application.route('/v1/multiply', methods=['GET', 'POST'])
def get_mult_res():
    first_num = request.args.get('first_num')
    second_num = request.args.get('second_num')
    res = float(first_num) * float(second_num) 
    return Response(json.dumps({'multiplication result': res}), mimetype='application/json', status=200)


# mutiple methods handling
# get example
# test get  
# curl -i http://"localhost:5000/v2/multiply?first_num=12.1&second_num=12"
# test post
# curl -i -X POST -d'{"first_num":1, "second_num":2}' -H "Content-Type: application/json" http://localhost:5000/v2/multiply

@application.route('/v2/multiply', methods=['GET', 'POST'])
def get_multiplication_res():
    first_num = 0
    second_num = 0 
    # if the method of the request is post
    if request.method == 'POST':
       # get post data  
       data = request.data
       # convert the json to dictionary
       data_dict = json.loads(data)
       # retreive the parameters
       first_num = data_dict.get('first_num',0)
       second_num =  data_dict.get('second_num',0)
    # if request method is not post (assuming get)
    else:
       first_num = request.args.get('first_num')
       second_num = request.args.get('second_num')
    res = float(first_num) * float(second_num) 
    return Response(json.dumps({'multiplication result': res}), mimetype='application/json', status=200)

# mock data
currency_rate = {
    'usd' : 3.3,
    'pound' : 4.5,
    'euro' : 4.8
}

@application.route('/calc/bit', methods=['GET'])
def post_currency_bit():
    return Response(json.dumps(get_bitcoin_index()), mimetype='application/json', status=200)


def get_bitcoin_index():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()['bpi']['USD']
    return response

if __name__ == "__main__":
    application.debug = True
    application.run()