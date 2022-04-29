import os
import boto3
from const import MSG_BOARD_TABLE_NAME

msg_board_table = boto3.resource('dynamodb').Table(os.environ[MSG_BOARD_TABLE_NAME])


def lambda_handler(event, context):
    response = msg_board_table.scan()
    msg_board_list = response.get('Items')

    return {
        'statusCode': 200,
        'body': msg_board_list
    }
