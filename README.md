     __          _______    _____                          
    /\ \        / / ____|  / ____|                         
   /  \ \  /\  / / (___   | |     ___  _   _ _ __ ___  ___ 
  / /\ \ \/  \/ / \___ \  | |    / _ \| | | | '__/ __|/ _ \
 / ____ \  /\  /  ____) | | |___| (_) | |_| | |  \__ \  __/
/_/    \_\/  \/  |_____/   \_____\___/ \__,_|_|  |___/\___|

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

in order to deploy to elasticbeanstalk

1. pip3 install awsebcli --upgrade
2. eb init -p python-3.7 flask-api-demo --region us-east-1
3. eb create flask-hellos

When modifying files use to update
eb deploy flask-hellos
in the end when we're all finished terminate the machines and delete them:
eb terminate flask-hellos