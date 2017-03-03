import json

restaurants_string = """[{
  "name" : "sweetgreen"
}]"""
print restaurants_string

restaurants_json = json.loads(restaurants_string)
print restaurants_json

class Restaurant:
  name = ""

  def __init__(self, data):
    self.name = self.getName(data)

  def getName(self, data):
    for i in data:
      return i['name']

restaurant_response = Restaurant(restaurants_json)
print restaurant_response.name


class GetALunchSpotResponse:
  restaurant = None

  def _init_(self, intent):
    self.restaurant = self.restaurants[0]

  def generateStringResponse():
    return "Why don't you go to: " + restaurant.name
