from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random


class Test(PLTestCase):
    def compare_feedback(self, ref_val, user_val):
        Feedback.add_feedback("expected: " + str(ref_val))
        Feedback.add_feedback("actual: " + str(user_val))
        Feedback.set_score(0)
        
    @points(1)
    @name("keys")
    def test_0(self):
        ref_val = self.ref.bens_berries
        user_val = self.st.bens_berries
        
        is_pass = True
        for key in ref_val.keys():
            if key not in user_val:
                is_pass = False
        if is_pass:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("values")
    def test_1(self):
        ref_val = self.ref.bens_berries
        user_val = self.st.bens_berries
        
        values = user_val.values()
        
        is_pass = True
        for value in ref_val.values():
            if value not in values:
                is_pass = False
        if is_pass:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)