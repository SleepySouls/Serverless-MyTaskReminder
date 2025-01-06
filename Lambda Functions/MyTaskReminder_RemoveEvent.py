import json
import boto3
import os

TableName = os.environ['TableName']
# Khởi tạo kết nối đến DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TableName)

def lambda_handler(event, context):
    try:      
        # Lấy EventID từ dữ liệu sự kiện
        event_id = event['EventID']

        # Kiểm tra xem EventID đã được cung cấp
        if not event_id:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing EventID')
            }

        # Xóa sự kiện từ DynamoDB
        response = table.delete_item(
            Key={
                'EventID': event_id
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Sự kiện đã được xóa khỏi cơ sở dữ liệu thành công')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Đã xảy ra lỗi: {}'.format(str(e)))
        }