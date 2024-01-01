# import os

## region = os.environ["MINHA_VAR"]


# def log(message):
#     print(region)
#     print(message)

import logging
from botocore.exceptions import NoCredentialsError
from boto3 import client

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
            logger.info("Objeto muito grande")
            return "Objeto muito grande"

        logger.info("Objeto de tamanho OK")
        return "Objeto de tamanho OK"

    except NoCredentialsError:
        logger.error("Credentials not available")
        return "Erro de credenciais"
    except Exception as e:
        logger.error(f"Error: {e}")
        return f"Erro: {e}"
