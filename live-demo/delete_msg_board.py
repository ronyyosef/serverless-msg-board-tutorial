import boto3

msg_board_table = boto3.resource('dynamodb').Table('msg-board-table')


def lambda_handler(event, context):
    pk = event.get('pk', None)
    if pk is None:
        return {
            'statusCode': 400,
            'body': 'pk pramter is required'
        }

    msg_board_table.delete_item(Key={'pk': pk})

    return {
        'statusCode': 200,
        'body': f'Message with pk {pk} was deleted'
    }
