# Websocket implementation for Serverless Framework with Python
#### uses Lambda-Functions and API-gateway


### setup
install packages with ```npm install``` and then deploy your function to AWS using ```sls deploy```. Make sure you have aws-cli and serverless-framework installed and configured


### usage
Connecting to it manually using something like Hoppscotch (or Postman) works with no issue. Doing this using a script (see client.js) is only possible if it is deployed on the same origin as the websocket itself, since as of now (11.1.24), API-gateway doesn't have support for enabling CORS.