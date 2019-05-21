Welcome!
---------

clone the repo: git clone https://github.com/UriBer/aws_elasticbeanstalk.git 
and do the following:
1. cd aws_elasticbeanstalk 
2. python3 -m venv venv
3. source venv/bin/activate
4. pip3 install -r requirements.txt
5. python application.py 
6. curl 127.0.0.1:5000
7. curl -X POST 127.0.0.1:5000
8. curl 127.0.0.1:5000/calc/currency/usd
8. curl 127.0.0.1:5000/calc/bit
see curl examples: https://www.keycdn.com/support/popular-curl-examples
see more on flask: http://flask.pocoo.org/docs/1.0/quickstart/

if you have already done the following just do steps: 1, 3, 5 in order to start the server.

in order to deploy to elasticbeanstalk:
-----

1. pip install awsebcli --upgrade
2. eb init -p python-3.6 flask-api-demo --region us-east-2
3. eb create flask-hellos

if you have problems when starting the eb env:
------
create iam user with keys, add aws-elasticbeanstalk-ec2-role and update it in the cloud9 bash using aws configure, type the 
please check your user in iam for the role: aws-elasticbeanstalk-ec2-role
see also: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/iam-instanceprofile.html

When modifying files use to update
------
eb deploy flask-hellos
in the end when we're all finished terminate the machines and delete them:
eb terminate flask-hellos

assignment
---------
before you'll do the assignment, please pull the latest version of the repo
using git pull https://github.com/UriBer/aws_elasticbeanstalk.git
1. create api endpoint that gets currency and amount and return the result.
2. create new get api that gets data from an open api and outputs the 
   data.