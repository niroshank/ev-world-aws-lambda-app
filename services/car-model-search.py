from __future__ import print_function

import os
import amazondax
import botocore.session

def lambda_handler(event, context):
    region = os.environ['REGION']
    
    session = botocore.session.get_session()
    #Store this at file level so that it is preserved between Lambda executions
    
    dynamodb = session.create_client('dynamodb', region_name=region) # low-level client
    table_name = "GetUrl-sample"
    
    def lambda_handler(event, context):
        try:
            response = dynamodb.put_item(TableName=table_name, Item={'id':'1', 'N': 'string'})
        except Exception, e:
            print(e)
        else:
            print("GetItem succeeded:")

