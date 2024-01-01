# import json
# import log


# def lambda_handler(event, context):
#     log.log(f"event: {event}")
#     # return {"statusCode": 200, "body": json.dumps(event)}
#     return {
#         "statusCode": 200,
#         "body": f"<html><body>Dados da requisicao {json.dumps(event)}</body></html>",
#         "headers": {"content-type": "text/html"},
#     }


# lambda_handler("aauau", "")


import log
from botocore.exceptions import NoCredentialsError
from boto3 import client

# Create an S3 client
s3_client = client("s3", region_name="sa-east-1")


def lambda_handler(event, context):
    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]

    try:
        # Get the object from S3
        response = s3_client.get_object(Bucket=bucket, Key=key)
        content_length = response["ContentLength"]

        mega_byte = 1024 * 1024

        if content_length > 1 * mega_byte:
            log.log("Objeto muito grande")
            return "Objeto muito grande"

        log.log("Objeto de tamanho OK")
        return "Objeto de tamanho OK"

    except NoCredentialsError:
        log.log("Credentials not available")
        return "Erro de credenciais"
    except Exception as e:
        log.log(f"Error: {e}")
        return f"Erro: {e}"
