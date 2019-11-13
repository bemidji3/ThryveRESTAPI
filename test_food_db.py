#!/usr/bin/env python3
from main import Food
import unittest

class TestFood(unittest.TestCase):
        """unit tests for python primer homework"""

        #@classmethod
        #def setUpClass(self):
        food_db = Food()

        def reset_data(self):
                "reset data is required because we cannot promise an order of test case execution"
                food_db = Food()

        def test_check_equals(self):
                self.reset_data()
                response = self.food_db.check_equals("203", .97)
                value = response["equal"]['Protein 0.97g'][0]
                self.assertEqual(value, "Acerola juice, raw")
        
        def test_check_under(self):
                self.reset_data()
                response = self.food_db.check_under("269", .2)
                value = response["under"]['Sugars, total 0.2g'][3]
                self.assertEqual(value, "Alfalfa seeds, sprouted, raw")

        def test_check_over(self):
                self.reset_data()
                response = self.food_db.check_over("204", 10)
                value = response["over"]['Total lipid (fat) 10g'][1]
                self.assertEqual(value, "Avocados, raw, all commercial varieties")

if __name__ == "__main__":
    unittest.main()

