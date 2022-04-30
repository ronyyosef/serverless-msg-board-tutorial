import boto3

msg_board_table = boto3.resource('dynamodb').Table('msg-board-table')


def lambda_handler(event, context):
    new_msg = event.get('msg')
    pk = event.get('pk')

    if new_msg is None or pk is None:
        return {
            'statusCode': 400,
            'body': 'pk and msg is required'
        }

    msg_board_table.update_item(
        Key={'pk': pk},
        UpdateExpression='SET msg = :msg',
        ExpressionAttributeValues={':msg': new_msg}
    )

    return {
        'statusCode': 200,
        'body': f"Update msg with pk {pk} to {new_msg}"
    }
