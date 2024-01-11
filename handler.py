import logging
import boto3
import json
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def send_to_connection(connection_id, url, data):
    gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=url)

    return gatewayapi.post_to_connection(
        ConnectionId=connection_id,
        Data=json.dumps(data).encode('utf-8')
    )


def connectionHandler(event, context):
    if event["requestContext"]["eventType"] == "CONNECT":
        logger.info("someone connected")

    elif event["requestContext"]["eventType"] == "DISCONNECT":
        logger.info("someone disconnected")

    else:
        url = "https://" + event["requestContext"]["domainName"] + "/" + event["requestContext"]["stage"]
        connection_id = event["requestContext"]["connectionId"]


        for i in range (10):
            time.sleep(1)

            data = {"progress": i * 10}
            send_to_connection(connection_id, url, data)


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
    }
