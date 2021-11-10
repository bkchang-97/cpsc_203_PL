import numpy as np


def generate(data):
    data['params']['names_for_user'] = []
    data["params"]["names_from_user"] = [
        {"name": "closet", "description": "a class to hold data and state about a closet", "type": "Python class"},
    ]