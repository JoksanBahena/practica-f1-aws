import json
import pymysql

def lambda_handler(event, context):

    connection = pymysql.connect(
        host="gymdiariolambda-relationaldatabase-gojnewewgdpp.czssy4oigfcr.us-east-1.rds.amazonaws.com",
        user="admin",
        password="'PU'h]9.8Q0+e'A%",
        database="Chomfit"
    )


    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM f1_drivers")
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            result_dict = [dict(zip(columns, row)) for row in result]
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,GET'
            },
            'body': json.dumps(result_dict)
        }
    except pymysql.MySQLError as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'false',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Methods': 'OPTIONS,GET'
            },
            'body': json.dumps({'error': str(e)})
        }
    finally:
        connection.close()
