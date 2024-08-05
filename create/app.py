import json
import pymysql


def lambda_handler(event, context):
    body = json.loads(event['body'])
    required_fields = ["id", "fullname", "team", "laps_completed", "race_completed"]

    for field in required_fields:
        if field not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f'{field} is required'})
            }

    connection = pymysql.connect(
        host="gymdiariolambda-relationaldatabase-gojnewewgdpp.czssy4oigfcr.us-east-1.rds.amazonaws.com",
        user="admin",
        password="'PU'h]9.8Q0+e'A%",
        database="Chomfit"
    )

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO f1_drivers (id, fullname, team, laps_completed, race_completed)  VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql,
                           (body['id'], body['fullname'], body['team'], body['laps_completed'], body['race_completed']))
        connection.commit()
        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'message': 'Car created successfully'})
        }
    except pymysql.MySQLError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'error': str(e)})
        }
    finally:
        connection.close()
