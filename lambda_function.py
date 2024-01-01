import json
import log


def lambda_handler(event, context):
    log.log(f"log de execução. event: {event}")
    # print(f"estou fazendo log: {event}")
    return {"statusCode": 200, "body": json.dumps(event)}


lambda_handler("aauau", "test")


# enviar code para aws lambda
# aws lambda update-function-code --function-name outraFuncao --zip-file fileb://lambda.zip
