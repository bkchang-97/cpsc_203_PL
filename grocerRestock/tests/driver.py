from typing import List, Tuple
from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    stu_num: int
    grade: float
    credits: int

