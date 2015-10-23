import unittest

class TestUM(unittest.TestCase):
    
    def setup(self):
        pass
    
    def test1(self):
        self.assertEqual([],[])
        
    def test2(self):
        self.assertEqual(1,1) 
        
if __name__ == '__main__':
    unittest.main()