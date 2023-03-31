"""
    sample tests
"""

from django.test import SimpleTestCase

from app import calc



class calcTests(SimpleTestCase):
    """Test the calc module"""
    
    def test_add_num(self):
        """Test adding numbers togheter"""
        res = calc.add(5,6)
        self.assertAlmostEqual(res,11)
        
        
    def test_subtract_sum(self):
        """Testing subtracting numbers"""
        
        res = calc.subtract(11,5)
        self.assertEqual(res,6)
    
    
    