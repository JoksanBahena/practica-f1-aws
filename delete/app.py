import json
import pymysql


def lambda_handler(event, context):
    body = json.loads(event['body'])
    id = body['id']

    connection = pymysql.connect(
        host="gymdiariolambda-relationaldatabase-gojnewewgdpp.czssy4oigfcr.us-east-1.rds.amazonaws.com",
        user="admin",
        password="'PU'h]9.8Q0+e'A%",
        database="Chomfit"
    )

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM carros WHERE id=%s"
            cursor.execute(sql, (id,))
        connection.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'message': 'Car deleted successfully'})
        }
    except pymysql.MySQLError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,DELETE'
            },
            'body': json.dumps({'error': str(e)})
        }
    finally:
        connection.close()
