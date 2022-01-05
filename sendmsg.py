import json
import urllib3
import boto3

client = boto3.client('apigatewaymanagementapi', endpoint_url="xxxxxxxxxx.com/production")

def lambda_handler(event, context):
    print(event)
    
    #Extract connectionId from incoming event
    connectionId = event["requestContext"]["connectionId"]
    
    #Do something interesting... 
    responseMessage = "responding..."
    
    #Form response and post back to connectionId
    response = client.post_to_connection(ConnectionId=connectionId, Data=json.dumps(responseMessage).encode('utf-8'))
    return { "statusCode": 200  }