cd ~/Practices/bittiger-fullstack/homework-xinxinhe/week6-codelab2

cd ~/Practices/bittiger-fullstack/homework-xinxinhe



Saturday: class notes 

Backend server
- mkdir `backend_server`
- create `vim service.py`
- `sudo pip install python-jsonrpc`
- `sudo killall python`
- go to server, mkdir rpc_client, `npm install --save jayson`
- go to rpc_client, create rpc_client.js
- create rpc_client_test.js , run `node rpc_client_test.js`
- run `python server.py`
- install mongoDB
- `sudo service mongod start`   `mongo`  `mongoimport --db test --collections news --drop week6_demo_news.json`
- manage pip install : requirements.txt   sudo pip install -r requirements.txt
- install pika



Node Serer 

MongoDB

ClouAMQP


Since react is using virtual DOM, so jQuery is declared in index.html

sudo mongoimport -d tap-news -c click_logs --type csv --file labeled_news.csv --headerline

I failed to install newspaper package. It shows errors like 'could not build the egg.'

This is because an error when installing nltk dependency. Try following commands:

$ sudo apt-get install python-dev

$ sudo apt-get install libxml2-dev libxslt-dev

$ sudo apt-get install libjpeg-dev zlib1g-dev libpng12-devpip

$ sudo pip install --upgrade setuptools

$ sudo pip install newspaper

If above still not works, try these: (Thanks to mwangxx0129)

Remove the repository version $ sudo apt-get remove python-setup tools

if necessary, install pip again $ wget https://bootstrap.pypa.io/get-pip.py; $ sudo -H python get-pip.py

install setuptools via pip $ sudo -H pip install -U pip setuptools

still failed repeat from start again



npm install -g react-scripts