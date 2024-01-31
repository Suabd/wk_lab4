import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    #test with a list of 2 pricess"
    def test_list_of_two_pricess(self):
        prices = [15,7]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    #test with a list 1 price
    def test_list_of_one_price(self):
        prices = [14]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    #test with list of 6 prices
    def test_list_of_six_prices(self):
        prices = [1,2.54,10,20,40,50]
        expected_discount = 1
        self.assertEqual(expected_discount, discount(prices))

    # test with string
    def test_list_of_strings(self):
        prices = [6,8,12]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    # test with float numbers
    def test_list_of_float(self):
        prices = [12.99,10.00,7.99]
        expected_discount = 7.99
        self.assertEqual(expected_discount, discount(prices))
    
    # what other data might this function have to deal with?
        # Probably floating point numbers, though error handling for non-number strings would be good.
   
    # remember a function has no control over how it is used
    # it may be called with any data - and it should be able to handle whatever data it gets appropriately

if __name__ == '__main__':
    unittest.main()