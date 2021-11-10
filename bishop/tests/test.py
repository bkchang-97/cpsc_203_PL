from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
import numpy as np
import random

class Test(PLTestCase):
    def compare_feedback(self, ref_val, user_val):
        Feedback.add_feedback("expected: " + str(ref_val))
        Feedback.add_feedback("actual: " + str(user_val))
        Feedback.set_score(0)
          
    def check_bool(self, ref, stu):
        return ref == stu
    
    @points(1)
    @name("NE Check")
    def test_0(self):
        coord1 = (3, 4)
        coord2 = (5, 2)
        ref_val = self.ref.moveBishop(coord1, coord2)
        stu_val = self.st.moveBishop(coord1, coord2)

        if self.check_bool(ref_val, stu_val):
            Feedback.add_feedback("moveBishop() looks good.")
            Feedback.set_score(1)
        else:
            self.compare_feedback(ref_val, stu_val)

    @points(1)
    @name("SE Check")
    def test_1(self):
        coord1 = (3, 4)
        coord2 = (6, 7)
        ref_val = self.ref.moveBishop(coord1, coord2)
        stu_val = self.st.moveBishop(coord1, coord2)

        if self.check_bool(ref_val, stu_val):
            Feedback.add_feedback("moveBishop() looks good.")
            Feedback.set_score(1)
        else:
            self.compare_feedback(ref_val, stu_val)

    @points(1)
    @name("NW Check")
    def test_2(self):
        coord1 = (3, 4)
        coord2 = (1, 2)
        ref_val = self.ref.moveBishop(coord1, coord2)
        stu_val = self.st.moveBishop(coord1, coord2)

        if self.check_bool(ref_val, stu_val):
            Feedback.add_feedback("moveBishop() looks good.")
            Feedback.set_score(1)
        else:
            self.compare_feedback(ref_val, stu_val)

    @points(1)
    @name("SW Check")
    def test_3(self):
        coord1 = (3, 4)
        coord2 = (2, 5)
        ref_val = self.ref.moveBishop(coord1, coord2)
        stu_val = self.st.moveBishop(coord1, coord2)

        if self.check_bool(ref_val, stu_val):
            Feedback.add_feedback("moveBishop() looks good.")
            Feedback.set_score(1)
        else:
            self.compare_feedback(ref_val, stu_val)

    @points(1)
    @name("Invalid")
    def test_4(self):
        coord1 = (3, 4)
        coord2 = (6, 4)
        ref_val = self.ref.moveBishop(coord1, coord2)
        stu_val = self.st.moveBishop(coord1, coord2)

        if self.check_bool(ref_val, stu_val):
            Feedback.add_feedback("moveBishop() looks good.")
            Feedback.set_score(1)
        else:
            self.compare_feedback(ref_val, stu_val)

