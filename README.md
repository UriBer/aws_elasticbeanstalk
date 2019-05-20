Welcome!
---------

pull the repo and do the following
1. cd to aws_elasticbeanstalk
2. python3 -m venv venv
3. source venv/bin/activate
4. pip3 install -r requirements.txt
5. python application.py 
6. curl 127.0.0.1:5000
7. curl -X POST 127.0.0.1:5000
8. curl 127.0.0.1:5000/calc/currency/usd
8. curl 127.0.0.1:5000/calc/bit
see curl examples: https://www.keycdn.com/support/popular-curl-examples

in order to deploy to elasticbeanstalk

1. pip install awsebcli --upgrade
2. eb init -p python-3.6 flask-api-demo --region us-east-2
3. eb create flask-hellos

When modifying files use to update
eb deploy flask-hellos
in the end when we're all finished terminate the machines and delete them:
eb terminate flask-hellos

assignment
---------
1. create api endpoint that gets currency and amount and return the result.
2. create new get api that gets data from an open api and outputs the 
   data.