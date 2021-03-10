from flask import Flask, Response, request
import json

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get_root():
    return Response(json.dumps({'Output': 'Hello Get World'}), mimetype='application/json', status=200)
    

@application.route('/', methods=['POST'])
def post_root():
    return Response(json.dumps({'Output': 'Hello Post World'}), mimetype='application/json', status=200)


@application.route('/chilki', methods=['POST'])
def post_req():
    return Response(json.dumps({'Output': 'Hello chilki '}), mimetype='application/json', status=200)


if __name__ == "__main__":
    application.debug = True
    application.run()