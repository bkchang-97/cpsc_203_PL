import random, copy
import prairielearn as pl
from collections import defaultdict

def grade(data):
    ans3 = data["submitted_answers"]["ans3"]
    ans4 = data["submitted_answers"]["ans4"]
    ans5 = data["submitted_answers"]["ans5"]
    
    if data['partial_scores']['ans3']['score'] == 0 and data['partial_scores']['ans4']['score'] == 0 and data['partial_scores']['ans5']['score'] == 0:
        d = defaultdict(bool)
        d[data['correct_answers']['ans3']] = True
        d[data['correct_answers']['ans4']] = True
        d[data['correct_answers']['ans5']] = True
        data['partial_scores']['ans3']['score'] = int(d[ans3])
        data['partial_scores']['ans4']['score'] = int(d[ans4])
        data['partial_scores']['ans5']['score'] = int(d[ans5])

    elif data['partial_scores']['ans3']['score'] == 0 and data['partial_scores']['ans4']['score'] == 0:
        d = defaultdict(bool)
        d[data['correct_answers']['ans3']] = True
        d[data['correct_answers']['ans4']] = True
        data['partial_scores']['ans3']['score'] = int(d[ans3])
        data['partial_scores']['ans4']['score'] = int(d[ans4])

    elif data['partial_scores']['ans3']['score'] == 0 and data['partial_scores']['ans5']['score'] == 0:
        d = defaultdict(bool)
        d[data['correct_answers']['ans3']] = True
        d[data['correct_answers']['ans5']] = True
        data['partial_scores']['ans3']['score'] = int(d[ans3])
        data['partial_scores']['ans5']['score'] = int(d[ans5])
        
    elif data['partial_scores']['ans5']['score'] == 0 and data['partial_scores']['ans4']['score'] == 0:
        d = defaultdict(bool)
        d[data['correct_answers']['ans5']] = True
        d[data['correct_answers']['ans4']] = True
        data['partial_scores']['ans5']['score'] = int(d[ans5])
        data['partial_scores']['ans4']['score'] = int(d[ans4])
        
    tot = 0
    for k in data['partial_scores']:
        tot += data['partial_scores'][k]['score']

    data["score"] = tot/10
    
