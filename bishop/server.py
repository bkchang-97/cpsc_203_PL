import numpy as np


def generate(data):
    data['params']['names_for_user'] = []
    data["params"]["names_from_user"] = [
        {"name": "moveBishop", "description": "a Python function", "type": "function"},
    ]
