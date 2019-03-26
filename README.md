      __          _______    _____                          
     /\ \        / / ____|  / ____|                         
    /  \ \  /\  / / (___   | |     ___  _   _ _ __ ___  ___ 
   / /\ \ \/  \/ / \___ \  | |    / _ \| | | | '__/ __|/ _ \
  / ____ \  /\  /  ____) | | |___| (_) | |_| | |  \__ \  __/
 /_/    \_\/  \/  |_____/   \_____\___/ \__,_|_|  |___/\___|
                                                            
                                                            
                                                            
Welcome!
---------

pull the repo and do the following
1. virtualenv .awsles1
2. source .awsles1/bin/activate
3. pip install requirements.txt
4. python application.py --port 8000 --debug
5. curl 127.0.0.1:8000

in order to deploy to elasticbeanstalk

1. pip install awsebcli --upgrade --user
2. eb init -p python-3.6 flask-api-demo
3. eb create flask-hellos
When modifying files use to update
eb deploy flask-hellos

