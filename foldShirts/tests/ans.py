from dataclasses import dataclass
from typing import List
from driver import shirt

@dataclass
class shirt:
    designer: str
    style: str
    folded: bool
    
    def fold(self):
        self.folded = True

@dataclass
class closet:
    shirts: List[shirt]
    
    def foldShirts(self):
        for shirt in self.shirts:
            shirt.fold()
        