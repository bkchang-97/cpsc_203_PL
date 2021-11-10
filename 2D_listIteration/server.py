import random, copy
import prairielearn as pl
import numpy as np

def generate(data):
    
    numbers = random.sample(range(1, 20), 16)
    
    target = random.choice(numbers)
    
    row1 = numbers[0:4]
    row2 = numbers[4:8]
    row3 = numbers[8:12]
    row4 = numbers[12:16]
    
    rows = [row1, row2, row3, row4]
    
    positions = random.sample(range(4, 16), 2)
    
    pos_a = 2
    a = rows[1][0]
    pos_b = positions[1]
    b = rows[(pos_b - 1) % 4][(pos_b - 1)//4]
    
    rendered_rows = [str(row1), str(row2), str(row3), str(row4)]
    
    data['params']['target'] = target
    data['params']['rows'] = rendered_rows
    data['params']['a'] = pos_a
    data['params']['b'] = pos_b
    
    data['correct_answers']['a'] = a
    data['correct_answers']['b'] = b
    