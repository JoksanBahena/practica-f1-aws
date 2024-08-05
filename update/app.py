import json
import pymysql
import os

def lambda_handler(event, context):
    body = json.loads(event['body'])
    id = body['id']

    if not id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'id is required'})
        }

    connection = pymysql.connect(
        host="gymdiariolambda-relationaldatabase-gojnewewgdpp.czssy4oigfcr.us-east-1.rds.amazonaws.com",
        user="admin",
        password="'PU'h]9.8Q0+e'A%",
        database="Chomfit"
    )

    try:
        with connection.cursor() as cursor:
            fields = ', '.join([f"{key}=%s" for key in body.keys()])
            values = list(body.values())
            values.append(id)
            sql = f"UPDATE carros SET {fields} WHERE noSerie=%s"
            cursor.execute(sql, values)
        connection.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,PUT'
            },
            'body': json.dumps({'message': 'Car updated successfully'})
        }
    except pymysql.MySQLError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,PUT'
            },
            'body': json.dumps({'error': str(e)})
        }
    finally:
        connection.close()
