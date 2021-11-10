from dataclasses import dataclass
from typing import List

#The initial implementation for Produce has been provided below

@dataclass
class Produce:
    name: str       # produce item
    fv: bool        # True if Fruit, False if Vegetable
    num: int        # quantity 
    