import boto3

msg_board_table = boto3.resource('dynamodb').Table('msg-board-table')


def lambda_handler(event, context):
    msg_board_list = msg_board_table.scan()

    return {
        'statusCode': 200,
        'body': msg_board_list['Items']
    }
