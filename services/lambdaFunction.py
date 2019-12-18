import json

def lambda_handler(event, context):
    response = "This is for test"
    return {"statusCode": 200, "body": json.dumps(response)}