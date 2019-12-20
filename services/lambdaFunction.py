import boto3
import json
import os
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal

ddb = boto3.resource('dynamodb')
table = ddb.Table('EvWorldCar')


def lambda_handler(event, context):
#   response = table.scan(
#       FilterExpression=Attr('payload.model').contains('Camry')
#       )
#   body = json.dumps(response['Items'], default=handle_decimal_type)
  return {
        'statusCode': 200,
        'body':json.dumps(event)
    }

def handle_decimal_type(obj):
  if isinstance(obj, Decimal):
      if float(obj).is_integer():
         return int(obj)
      else:
         return float(obj)
  raise TypeError
  