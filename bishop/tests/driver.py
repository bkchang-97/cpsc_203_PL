import pandas as pd
from dataclasses import dataclass, field


@dataclass
class Student:
  name: str
  favo_num: int
  student_num: int
  major: str
  required_time: int

  def greet(self):
    return "Hello! My name is " + self.name + " and my favorite number is " + str(self.favoNum) + ". I am majoring " + self.major + " I need " + self.requiredTime + " minutes with a TA." 
