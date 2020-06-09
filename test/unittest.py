import unittest
from code.datamunger import *

class TestDatamunger(unittest.TestCase):
    

    def test_CalculateTotalFunction(self):
        temp= [26,73,35,86,99,10,102,199,0]
        value = datamunger.calc_total(temp)
        self.assertEqual(value, 604)


    def test_check_row_function(self):
        
        temp= [10,28,29,62,78,92,867,999,1203,456]
        temp2=[]
        value= datamunger.check_row(4,temp2, temp) # assign random value for n
        self.assertEqual(value, True)

    def test_check_row_function_letters(self):
        temp= [10,28,29,'a',78,92,867,999,1203,456]
        temp2=[]
        value= datamunger.check_row(4,temp2, temp) # assign the sam value for n as in previous case
        self.assertEqual(value, False)

    def test_check_row_function_blanks(self):
        temp= [10,28,29,' ',78,92,867,999,1203,456]
        temp2=[]
        value= datamunger.check_row(4,temp2, temp) # assign the sam value for n as in previous case
        self.assertEqual(value, False)
    



if __name__== '__main__':
    unittest.main()