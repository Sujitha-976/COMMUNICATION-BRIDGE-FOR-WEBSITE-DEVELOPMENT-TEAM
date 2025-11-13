
import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('n8nWorkflowLogs')

def lambda_handler(event, context):
    item = event
    if 'executionId' not in item:
        item['executionId'] = str(uuid.uuid4())
    if 'timestamp' not in item:
        item['timestamp'] = datetime.utcnow().isoformat()

    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'ok', 'message': 'Log saved to DynamoDB'})
    }
