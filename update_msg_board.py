import os
import boto3
from const import MSG_BOARD_TABLE_NAME

msg_board_table = boto3.resource('dynamodb').Table(os.environ[MSG_BOARD_TABLE_NAME])


def lambda_handler(event, context):
    pk = event.get('path').get('pk', None)
    new_msg = event.get('body').get('msg', None)
    if pk is None or new_msg is None:
        return {
            'statusCode': 400,
            'body': 'Bad Request'
        }

    msg_board_table.update_item(
        Key={
            'pk': pk
        },
        UpdateExpression='SET msg = :msg',
        ExpressionAttributeValues={
            ':msg': new_msg
        }
    )

    return {
        'statusCode': 200,
        'body': f'item {pk} was updated'
    }
