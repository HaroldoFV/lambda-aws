import json
import log


def lambda_handler(event, context):
    log.log(f"event: {event}")
    return {"statusCode": 200, "body": json.dumps(event)}


lambda_handler("aauau", "")
