import uuid
import boto3

msg_board_table = boto3.resource('dynamodb').Table('msg-board-table')


def lambda_handler(event, context):
    pk = uuid.uuid4()
    msg = event.get('msg', None)

    if msg is None:
        return {
            'statusCode': 400,
            'body': "msg is required"
        }

    msg_board_table.put_item(Item=
                             {'pk': str(pk), "msg": msg})

    return {
        'statusCode': 200,
        'body': f'Message with pk {pk} was added'
    }
