from dataclasses import dataclass
from typing import List

#The initial implementation for Produce has been provided below

@dataclass
class Produce:
    name: str       # produce item
    fv: bool        # True if Fruit, False if Vegetable
    num: int        # quantity 
    
    def needsRestock(self, min_quantity):
        return self.num <= min_quantity

@dataclass
class Grocer:
    name: str
    city: str
    restock: int
    min_restock: int
    lop: List[Produce]
    
    def restockProduce(self):
        for p in self.lop:
            if p.needsRestock(self.min_restock):
                p.num += self.restock
        