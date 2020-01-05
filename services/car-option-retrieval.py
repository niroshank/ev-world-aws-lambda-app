import boto3
import json
import os
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['DDB'])

def lambda_handler(event, context):
    dataObject = json.loads(event['body'])
    response = table.query(
      KeyConditionExpression=Key('id').eq(dataObject["id"])
      )
    
    options = response['Items'][0]['payload']['options']
    body = json.dumps(options, default=handle_decimal_type)
    return {
        'statusCode': 200,
        'body': body
    }

def handle_decimal_type(obj):
  if isinstance(obj, Decimal):
      if float(obj).is_integer():
         return int(obj)
      else:
         return float(obj)
  raise TypeError
  