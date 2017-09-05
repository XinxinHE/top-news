#!/bin/bash
service redis_6379 start
service mongod start

pip install -r requirements.txt

fuser -k 4040/tcp
fuser -k 5050/tcp
fuser -k 3000/tcp
fuser -k 3001/tcp
killall python

cd web_server/server 
npm start &

cd ../client
npm run start &

cd ../../backend_server
#4040
python service.py &

cd ../news_recommendation_service
#5050
python recommendation_service.py &

echo "=============================================="
read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES. " PRESSKEY

kill $(jobs -p)