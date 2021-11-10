import numpy as np


def generate(data):
    data['params']['names_for_user'] = [
        {"name": "Produce", "description": "a dataclass to hold data about produce", "type": "Python dataclass"},
        ]
    data["params"]["names_from_user"] = [
        {"name": "Produce", "description": "a fully implemented dataclass about a Produce item, the implementation has been partially completed for you below", "type": "Python dataclass"},
        {"name": "Grocer", "description": "a dataclass to hold data about a Grocer", "type": "Python dataclass"},
        {"name": "needsRestock", "description": "a member function for Produce that determines if a produce item needs restocking or not, takes an additional parameter that represents the minimum threshold a Produce item needs to reach before requiring restocking", "type": "Python function"},
        {"name": "restockProduce", "description": "a member function for Grocer that restocks all produce items (that need restocking) by the restock number, takes no additional parameters and does not return anything (it modifies the Grocer's list of produce)", "type": "Python function"}
    ]