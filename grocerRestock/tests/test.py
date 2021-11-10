from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps


class Test(PLTestCase):
    def compare_feedback(self, ref_val, user_val):
        Feedback.add_feedback("expected: " + str(ref_val))
        Feedback.add_feedback("actual: " + str(user_val))
        Feedback.set_score(0)
    
    def checkGrocerConstructor(self, ref_val, user_val):
        if ref_val.name != user_val.name:
            return False
            
        if ref_val.city != user_val.city:
            return False
            
        if ref_val.restock != user_val.restock:
            return False
            
        if ref_val.min_restock != user_val.min_restock:
            return False
        
        for i in range(len(ref_val.lop)):
            if ref_val.lop[i] != user_val.lop[i]:
                return False
                
        return True

    def checkNeedsRestock(self, ref_val, user_val, minq):
        return ref_val.needsRestock(minq) == user_val.needsRestock(minq)
        
    def checkRestockProduce(self, ref_val, user_val):
        ref_val.restockProduce()
        user_val.restockProduce()
        
        ref_total = 0
        stu_total = 0
        
        for i in range(len(ref_val.lop)):
            ref_total += ref_val.lop[i].num
            stu_total += user_val.lop[i].num
        
        return ref_total == stu_total
        
        
    @points(1)
    @name("courseConstructor")
    def test_0(self):
        p1 = self.ref.Produce("Apple", True, 25)
        p2 = self.ref.Produce("Celery", False, 10)
        p3 = self.ref.Produce("Kale", False, 5)
        p4 = self.ref.Produce("Mangosteen", True, 12)
        p5 = self.ref.Produce("Strawberry", True, 21)
    
        p_list = [p1, p2, p3, p4, p5]
        grocer_ref = self.ref.Grocer("LFM", "Coquitlam", 10, 10, p_list)
        grocer_stu = self.st.Grocer("LFM", "Coquitlam", 10, 10, p_list)
        
        if self.checkGrocerConstructor(grocer_ref, grocer_stu):
            Feedback.set_score(1)
        else:
            self.compare_feedback(grocer_ref, grocer_stu)
    
    @points(1)
    @name("needsRestock10")
    def test_1(self):
        p1a = self.ref.Produce("Apple", True, 25)
        p2a = self.ref.Produce("Celery", False, 10)
        p1b = self.st.Produce("Apple", True, 25)
        p2b = self.st.Produce("Celery", False, 10)
        
        if self.checkNeedsRestock(p1a, p1b, 10):
            Feedback.set_score(0.5)
        if self.checkNeedsRestock(p2a, p2b, 10):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)
    
    @points(1)
    @name("needsRestock22")
    def test_2(self):
        p5a = self.ref.Produce("Strawberry", True, 21)
        p5b = self.st.Produce("Strawberry", True, 21)
        if self.checkNeedsRestock(p5a, p5b, 22):
            Feedback.set_score(1)
        else:
            self.compare_feedback(p5a.needsRestock(22), p5b.needsRestock(22))
    
    @points(1)
    @name("restockProduce10")
    def test_3(self):
        p1 = self.ref.Produce("Apple", True, 25)
        p2 = self.ref.Produce("Celery", False, 10)
        p3 = self.ref.Produce("Kale", False, 5)
        p4 = self.ref.Produce("Mangosteen", True, 12)
        p5 = self.ref.Produce("Strawberry", True, 21)

        p6 = self.ref.Produce("Apple", True, 25)
        p7 = self.ref.Produce("Celery", False, 10)
        p8 = self.ref.Produce("Kale", False, 5)
        p9 = self.ref.Produce("Mangosteen", True, 12)
        p10 = self.ref.Produce("Strawberry", True, 21)
        p_list = [p1, p2, p3, p4, p5]
        p_list2 = [p6, p7, p8, p9, p10]
        
        grocer_ref = self.ref.Grocer("LFM", "Coquitlam", 10, 10, p_list)
        grocer_stu = self.st.Grocer("LFM", "Coquitlam", 10, 10, p_list2)
        
        if self.checkRestockProduce(grocer_ref, grocer_stu):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("needsRestock22")
    def test_4(self):
        p1 = self.ref.Produce("Apple", True, 25)
        p2 = self.ref.Produce("Celery", False, 10)
        p3 = self.ref.Produce("Kale", False, 5)
        p4 = self.ref.Produce("Mangosteen", True, 12)
        p5 = self.ref.Produce("Strawberry", True, 21)

        p6 = self.ref.Produce("Apple", True, 25)
        p7 = self.ref.Produce("Celery", False, 10)
        p8 = self.ref.Produce("Kale", False, 5)
        p9 = self.ref.Produce("Mangosteen", True, 12)
        p10 = self.ref.Produce("Strawberry", True, 21)
        p_list = [p1, p2, p3, p4, p5]
        p_list2 = [p6, p7, p8, p9, p10]
        
        grocer_ref = self.ref.Grocer("SG", "Vancouver", 7, 22, p_list)
        grocer_stu = self.st.Grocer("SG", "Vancouver", 7, 22, p_list2)
        
        if self.checkRestockProduce(grocer_ref, grocer_stu):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)