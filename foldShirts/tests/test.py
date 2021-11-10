from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps


class Test(PLTestCase):
    def compare_feedback(self, ref_val, user_val):
        Feedback.add_feedback("expected: " + str(ref_val))
        Feedback.add_feedback("actual: " + str(user_val))
        Feedback.set_score(0)
        
    @points(1)
    @name("closetConstructor")
    def test_0(self):
        shirt_1 = self.ref.shirt("red", "a", False)
        shirt_2 = self.ref.shirt("blue", "b", True)
        shirt_3 = self.ref.shirt("yellow", "c", False)
        closet_ref = self.ref.closet([shirt_1, shirt_2, shirt_3])
        closet_stu = Feedback.call_user(self.st.closet, [shirt_1, shirt_2, shirt_3])
        
        is_pass = True
        if Feedback.check_list("closetTest", closet_ref.shirts, closet_stu.shirts):
            for i in range(len(closet_ref.shirts)):
                if closet_ref.shirts[i].designer != closet_stu.shirts[i].designer:
                    self.compare_feedback(closet_ref.shirts[i], closet_stu.shirts[i])
                    is_pass = False
            if is_pass:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        else:
            self.compare_feedback(closet_ref, closet_stu)

    @points(1)
    @name("closetFold")
    def test_1(self):
        shirt_1 = self.ref.shirt("red", "a", False)
        shirt_2 = self.ref.shirt("blue", "b", True)
        shirt_3 = self.ref.shirt("yellow", "c", False)
        closet_ref = self.ref.closet([shirt_1, shirt_2, shirt_3])
        closet_stu = Feedback.call_user(self.st.closet, [shirt_1, shirt_2, shirt_3])
        
        closet_ref.foldShirts()
        closet_stu.foldShirts()
        
        is_pass = True
        if Feedback.check_list("closetTest", closet_ref.shirts, closet_stu.shirts):
            for i in range(len(closet_ref.shirts)):
                if closet_ref.shirts[i].folded != closet_stu.shirts[i].folded:
                    self.compare_feedback(closet_ref.shirts[i], closet_stu.shirts[i])
                    is_pass = False
            if is_pass:
                Feedback.set_score(1)
            else:
                Feedback.set_score(0)
        else:
            self.compare_feedback(closet_ref, closet_stu)