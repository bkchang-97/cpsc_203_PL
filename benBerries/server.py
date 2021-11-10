import numpy as np


def generate(data):
    data['params']['names_for_user'] = []
    data["params"]["names_from_user"] = [
        {"name": "bens_berries", "description": "stores berry counts", "type": "dictionary"},
    ]