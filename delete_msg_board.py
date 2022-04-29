import os
import boto3
from const import MSG_BOARD_TABLE_NAME

msg_board_table = boto3.resource('dynamodb').Table(os.environ[MSG_BOARD_TABLE_NAME])


def lambda_handler(event, context):
    pk = event.get('path', {}).get('pk', None)

    if pk is None:
        return {
            'statusCode': 400,
            'body': 'pk is required'
        }

    msg_board_table.delete_item(
        Key={
            'pk': pk
        }
    )

    return {
        'statusCode': 200,
        'body': 'Item deleted',
    }
