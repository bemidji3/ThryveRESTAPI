from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import json
import collections
from pprint import pprint


app = Flask(__name__)
api = Api(app)


class Food(Resource):

    def __init__(self):
        self.nutrient_ids = {
            '203': "Protein",
            '204': "Total lipid (fat)",
            '205': "Carbohydrate, by difference",
            '269': "Sugars, total"
        }

        with open('food_data.json') as json_file:
            self.data = json.load(json_file)

        self.foods = self.data["report"]["foods"]
        self.post_response = collections.defaultdict(dict)

    def check_equals(self, match_nutrient, amount):
        self.post_response['equal'][self.nutrient_ids[match_nutrient] + ' ' + str(amount) + 'g'] = []
        for food in self.foods:
            for food_nutrient in food['nutrients']:
                if food_nutrient["nutrient_id"] == match_nutrient and food_nutrient["value"] != '--':
                    if float(food_nutrient["value"]) == float(amount):
                        self.post_response['equal'][food_nutrient["nutrient"] + ' ' + str(amount) + 'g'].append(food["name"])

    def check_under(self, match_nutrient, amount):
        self.post_response['under'][self.nutrient_ids[match_nutrient] + ' ' + str(amount) + 'g'] = []
        for food in self.foods:
            for food_nutrient in food['nutrients']:
                if food_nutrient["nutrient_id"] == match_nutrient and food_nutrient["value"] != '--':
                    if float(food_nutrient["value"]) < float(amount):
                        self.post_response['under'][food_nutrient["nutrient"] + ' ' + str(amount) + 'g'].append(food["name"])

    def check_over(self, match_nutrient, amount):
        self.post_response['over'][self.nutrient_ids[match_nutrient] + ' ' + str(amount) + 'g'] = []
        for food in self.foods:
            for food_nutrient in food['nutrients']:
                if food_nutrient["nutrient_id"] == match_nutrient and food_nutrient["value"] != '--':
                    if float(food_nutrient["value"]) > float(amount):
                        self.post_response['over'][food_nutrient["nutrient"] + ' ' + str(amount) + 'g'].append(food["name"])

    def filter_check(self, nutrient, flag, amount):
        if flag == 'under':
            self.check_under(nutrient, amount)
        elif flag == 'equal':
            self.check_equals(nutrient, amount)
        elif flag == 'over':
            self.check_over(nutrient, amount)

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("over", type=dict)
        parser.add_argument("under", type=dict)
        parser.add_argument("equal", type=dict)

        args = parser.parse_args()

        print(args)

        over = args['over']
        under = args['under']
        equals = args['equal']

        for nutrient in over:
            print('checking over!')
            self.filter_check(nutrient,'over',over[nutrient])
        for nutrient in under:
            self.filter_check(nutrient, 'under', under[nutrient])
        for nutrient in equals:
            self.filter_check(nutrient, 'equal', equals[nutrient])


        print("post response: ")
        pprint(self.post_response)

        return self.post_response


api.add_resource(Food, "/food/return")

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response



if __name__ == '__main__':
    app.run(debug=True)









