from unittest import TestCase,main
from function import divide,multiplication

class Testresult(TestCase):
    def test_myfun(self):
        dividend=15
        divisor=3
        result_expected=5.0001
        # self.assertEqual(divide(dividend,divisor),result_expected)
        
        self.assertAlmostEqual(divide(dividend,divisor),result_expected,delta=0.0001)
        
        
    def test_negative(self):
        dividend=15
        divisor=-3
        result_expected=-5.0
        # self.assertEqual(divide(dividend,divisor),result_expected)
        
        self.assertAlmostEqual(divide(dividend,divisor),result_expected,delta=0.0001)
    
    
    def test_error_division(self):
        # with self.assertRaises(ZeroDivisionError):
        #     divide(25,0)
        self.assertRaises(ZeroDivisionError, lambda : divide(25,0))  #shortest way to write 
    
    def test_multiplication(self):
        with self.assertRaises(ValueError):
            multiplication()
            
    
    def test_singleval(self):
        expect=10
        
        self.assertEqual(multiplication(expect),expect)
    
    def test_result(self):
        expected_result=15
        
        self.assertEqual(multiplication(3,5),expected_result)

if __name__=="__main__":
    main()