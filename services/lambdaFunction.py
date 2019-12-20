from __future__ import print_function # Python 2/3 compatibility
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EvWorldCar')

def lambda_handler(event, context):    
    print("Joe's music")
    print(table.creation_date_time)

response = table.query(
    KeyConditionExpression=Key('id').eq(1)
)

for i in response['Items']:
    print(i['id'], ":", i['id'])

