import json
import boto3
import decimal
from boto3.dynamodb.conditions import Key
 
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JBuzzy')

def lambda_handler(event, context):
    earliest = 0
    if 'queryStringParameters' in event and 'since' in event['queryStringParameters']:
        earliest = int(event['queryStringParameters']['since'])
    # TODO this is all horribly not optimized!
    response = table.scan(
        FilterExpression=Key('datetime').gt(earliest)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({'items': sorted(response['Items'], key = lambda i: i['datetime'])}, default=decimal_default)
    }