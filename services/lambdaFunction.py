import json

def lambda_handler(event, context):
    response = "Hello, Everything fine"
    return {"statusCode": 200, "body": json.dumps(response)}