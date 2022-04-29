import uuid
import os
import boto3
from const import MSG_BOARD_TABLE_NAME

msg_board_table = boto3.resource('dynamodb').Table(os.environ[MSG_BOARD_TABLE_NAME])


def lambda_handler(event, context):
    pk = uuid.uuid4()
    msg = event.get('body').get('msg')
    if msg is None:
        return {
            'statusCode': 400,
            'body': 'msg is required'
        }

    msg_board_table.put_item(
        Item={
            'pk': str(pk),
            'msg': msg
        })

    return {"statusCode": 200, "body": f'{str(pk)} was added'}
