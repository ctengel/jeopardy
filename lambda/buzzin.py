import json
import time
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JBuzzy')

def lambda_handler(event, context):
    indata = json.loads(event['body'])
    item = {
        'person': indata['person'],
        'datetime': int(time.time()*1000.0)
    }
    response = table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }