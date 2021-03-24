import json


def get_config(key):
    with open("../config.json") as f:
        config = json.load(f)
    return config[key]
