import os

region = os.environ["MINHA_VAR"]


def log(message):
    print(region)
    print(message)
