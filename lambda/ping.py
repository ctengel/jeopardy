import json
import time


def lambda_handler(event, context):
    item = {
        'datetime': int(time.time()*1000.0)
    }
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
