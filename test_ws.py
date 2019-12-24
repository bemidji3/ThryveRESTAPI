#!/usr/bin/env python3
import unittest
import requests
import json
from collections import defaultdict


class TestWebserver(unittest.TestCase):

    # def __init__(self):
    #     self.URL = "http://127.0.0.1:5000/food/return"

    def test_check_under(self):
        URL = "http://127.0.0.1:5000/food/return"
        PARAMS = {}
        PARAMS['under'] = {'205': 0.5}
        PARAMS['equal'] = {}
        PARAMS['over'] = {}
        headers = {'content-type': 'application/json'}

        req = requests.post(url=URL, json=PARAMS, headers=headers)
        res = req.json()



        under = res["under"][ "Carbohydrate, by difference 0.5g"]

        self.assertEqual(under, [
          "Alcoholic beverage, beer, light",
          "Alcoholic beverage, beer, light, BUD LIGHT",
          "Alcoholic beverage, beer, light, BUDWEISER SELECT",
          "Alcoholic beverage, beer, light, low carb",
          "Alcoholic beverage, distilled, all (gin, rum, vodka, whiskey) 86 proof",
          "Alcoholic beverage, distilled, whiskey, 86 proof",
          "Alcoholic beverage, wine, cooking",
          "Alcoholic beverage, wine, light",
          "Alcoholic beverages, beer, higher alcohol",
          "Arugula, raw"
            ])


    def test_check_equals(self):
        URL = "http://127.0.0.1:5000/food/return"
        PARAMS = {}
        PARAMS['under'] = {}
        PARAMS['equal'] = {'203': 1}
        PARAMS['over'] = {}
        headers = {'content-type': 'application/json'}

        req = requests.post(url=URL, json=PARAMS, headers=headers)
        res = req.json()


        equal = res['equal']['Protein 1g']

        self.assertEqual(equal, [
            "Babyfood, Baby MUM MUM Rice Biscuits",
            "Babyfood, banana with mixed berries, strained",
            "Babyfood, cereal, oatmeal, with bananas, dry"
            ])


    def test_check_over(self):
        URL = "http://127.0.0.1:5000/food/return"

        PARAMS = {}
        PARAMS['under'] = {}
        PARAMS['equal'] = {}
        PARAMS['over'] = {'203': 5}
        headers = {'content-type': 'application/json'}

        req = requests.post(url=URL, json=PARAMS, headers=headers)



        res = req.json()

        over = res["over"]["Protein 5g"]


        self.assertEqual(over, [
            "Amaranth grain, uncooked",
            "Artichokes, (globe or french), frozen, cooked, boiled, drained, without salt",
            "Asparagus, canned, drained solids",
            "Asparagus, frozen, cooked, boiled, drained, without salt"
        ])


if __name__ == '__main__':
    unittest.main()



