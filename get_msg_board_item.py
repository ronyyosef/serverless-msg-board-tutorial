import os
import boto3
from const import MSG_BOARD_TABLE_NAME

msg_board_table = boto3.resource('dynamodb').Table(os.environ[MSG_BOARD_TABLE_NAME])


def lambda_handler(event, context):
    pk = event.get('path', {}).get('pk', None)

    item = msg_board_table.get_item(
        Key={
            'pk': pk,
        }
    )

    if 'Item' not in item:
        return {
            'statusCode': 404,
            'body': 'Item not found'
        }

    return {
        'statusCode': 200,
        'body': item['Item']
    }
