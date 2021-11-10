from typing import List, Tuple
from dataclasses import dataclass, field


@dataclass
class shirt:
    designer: str
    style: str
    folded: bool
    
    def fold(self):
        self.folded = True
