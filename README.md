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

in order to deploy to elasticbeanstalk

1. pip install awsebcli --upgrade
2. eb init -p python-3.6 flask-api-demo
3. eb create flask-hellos
When modifying files use to update
eb deploy flask-hellos

