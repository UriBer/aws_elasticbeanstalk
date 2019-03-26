from flask import Flask, Response, request
import json

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)
    
if __name__ == "__main__":
    application.debug = True
    application.run()