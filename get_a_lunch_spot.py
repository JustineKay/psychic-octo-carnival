import json

restaurants_string = """[{
  "name" : "sweetgreen"
}]"""

class Restaurant:
  name = ""
  def __init__(self, data):
    self.name = data['name']


class GetALunchSpotResponse:
  restaurant = None

  def _init_(self, intent):
    self.restaurant = self.restaurants[0]

  def generateStringResponse():
    return "Why don't you go to: " + restaurant.name


print restaurants_string
restaurants_json = json.loads(restaurants_string)
print restaurants_json

first_restaurant = Restaurant(restaurants_json[0])
print first_restaurant.name

