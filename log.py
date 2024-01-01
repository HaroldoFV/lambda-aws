import os

region = os.environ["AWS_REGION"]


def log(message):
    print(region)
    print(message)
