import json
from pprint import pprint
from random import randrange

class Restaurant:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences

    # checks for strict accomodation
    def can_accomodate(self, desired):
        for d in desired:
            if d not in self.preferences:
                # as long as one strict requirement cannot be met, return false
                return False

        # otherwise all checks pass, return True
        return True

    @classmethod
    def fromJSON(cls, data):
        r = Restaurant(data["name"], [])
        return r

class DietaryPreference:
    """
    is_strict: used to indicate whether the restriction is strict or not.
               When applied to a person, indicates whether the preference is
               actually a restriction, for example:
               DietaryPreference("vegan", True) -> strict conformance to vegan
               DietaryPreference("meat", False) -> prefer meat, but not strictly
               DietaryPreference("cilatro", False, True) -> do not prefer cilantro,
                                                            but not strictly
               When applied to a restaurant, indicates whether the preference
               is fulfilled by the restaurant:
               DietaryPreference("vegan", False) -> Serves vegan, but only vegan
    inverse:   See examples above, but it inverts the choice, so:

               DietaryPreference("thai", False, False) -> Prefer thai
               DietaryPreference("thai", False, True) -> Prefer not thai
               DietaryPreference("thai", True True) -> Cannot have thai(loser)
    """
    def __init__(self, name, is_strict, inverse=False):
        self.name = name
        self.is_strict = is_strict
        self.inverse = inverse

    def __eq__(self, other):
        return other.name.lower() == self.name.lower()

class Person:
    def __init__(self, canonical_name, preferences=[]):
        self.canonical_name = canonical_name
        self.preferences = preferences

    def matches(self, name):
        #for now, just lowercase and do any sort of partial string compare
        return self.canonical_name.lower() == name.lower()

def find_person(person_list, name):
    for p in person_list:
        if p.matches(name):
            return p


class GetALunchSpotIntent:
  def __init__(self, alexa_intent):
      self.people = alexa_intent.get_slot_map()["Person"].split()
      self.people = [p for p in filter(lambda s: s not in ["and", "everyone", "team", "everybody"], self.people)]
      self.people = map(lambda name: find_person(persons, name), self.people)

class GetALunchSpotResponse:
    restaurant = None

    def __init__(self, alexa_intent):
        self.intent = GetALunchSpotIntent(alexa_intent)
        self.restaurant = restaurants[0]

    def find_restaurant(self):
        preferences = [prefs for person in self.intent.people for prefs in person.preferences]

        # always accomodate strict preferences
        strict = filter(lambda pref: pref.is_strict, preferences)

        # find all restaurants that match the strict criteria
        eligible = filter(lambda r: r.can_accomodate(strict), restaurants)
        pprint([r.name for r in eligible])

        return eligible[randrange(0, len(eligible))]


restaurants_string = """[{
  "name" : "sweetgreen"
}]"""
restaurants_json = json.loads(restaurants_string)

restaurants = [
Restaurant("Sweetgreen", [DietaryPreference("vegan", False), DietaryPreference("vegetarian", False), DietaryPreference("gluten-free", False)]),
Restaurant("Thai Villa", [DietaryPreference("vegan", False), DietaryPreference("vegetarian", False), DietaryPreference("gluten-free", False)]),
Restaurant("Ribalta", []),
Restaurant("Vapiano", []),
Restaurant("Friend of a Farmer", [])
]

persons = [
Person("Colden", []),
Person("Cara", [DietaryPreference("gluten-free", True)]),
Person("Helen", [DietaryPreference("gluten-free", True), DietaryPreference("vegan", True)]),
Person("Justine", [DietaryPreference("gluten-free", True), DietaryPreference("vegan", True)]),
Person("Rads", [DietaryPreference("vegetarian", True)]),
Person("David", [DietaryPreference("meat", False)]),
Person("Ying"),
Person("Tom")
]
