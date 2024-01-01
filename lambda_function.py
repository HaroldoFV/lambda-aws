import json
import log


def lambda_handler(event, context):
    log.log(f"event: {event}")
    # return {"statusCode": 200, "body": json.dumps(event)}
    return {
        "statusCode": 200,
        "body": f"<html><body>Dados da requisicao {json.dumps(event)}</body></html>",
    }


lambda_handler("aauau", "")
