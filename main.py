from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
import json
import collections
from pprint import pprint
import operator


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

        self.ops = {
            '>' : operator.gt,
            '=' : operator.eq,
            '<' : operator.lt
        }

        with open('food_data.json') as json_file:
            self.data = json.load(json_file)

        self.foods = self.data["report"]["foods"]
        self.post_response = collections.defaultdict(dict)

    def check(self, match_nutrient, amount, flag, op):
        self.post_response[flag][self.nutrient_ids[match_nutrient] + ' ' + str(amount) + 'g'] = []
        for food in self.foods:
            for food_nutrient in food['nutrients']:
                if food_nutrient["nutrient_id"] == match_nutrient and food_nutrient["value"] != '--':
                    if self.ops[op](float(food_nutrient["value"]),float(amount)):
                        self.post_response[flag][food_nutrient["nutrient"] + ' ' + str(amount) + 'g'].append(food["name"])

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
            self.check(nutrient,over[nutrient], 'over', '>')
        for nutrient in under:
            self.check(nutrient, under[nutrient], 'under', '<')
        for nutrient in equals:
            self.check(nutrient, equals[nutrient], 'equal', '=')

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









