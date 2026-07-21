from unittest import TestCase,main
from classes import print,PrinterError

class TestPrinter(TestCase):
    
    def setUp(self):   #setUp ek method h to set testcase
        self.print_obj=print(page_per_s=3.0,capacity=200)
    def test_class(self): 
        # print_obj=print(page_per_s=2.0 , capacity= 300)
        self.print_obj.prinitng(25)
        
        
    def test_capacity(self):
        with self.assertRaises(PrinterError):
            self.print_obj.prinitng(276)

if __name__=="__main__":
    main()
