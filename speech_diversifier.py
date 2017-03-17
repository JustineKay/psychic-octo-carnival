from random import randrange

class SpeechDiversifier:
    def __init__(self):
      suggestions_list = []
      suggestions_list.append("How about {TOKEN}")
      suggestions_list.append("What about {TOKEN}")
      suggestions_list.append("Today seems like a good day for {TOKEN}")
      suggestions_list.append("Hmm... it's been awhile since {TOKEN}")
      suggestions_list.append("Ok, maybe {TOKEN}?")
      suggestions_list.append("Maybe {TOKEN} today?")
      self.suggestions = {}
      for i in xrange(len(suggestions_list)):
          self.suggestions[i] = suggestions_list[i]

    """
    Takes a restaurant name and returns differences utterances to suggest it.
    """
    def diversify_suggestion(self, name):
        return self.suggestions[randrange(0, len(self.suggestions))].format(TOKEN=name)

    def could_not_find(self):
        could_not_find = [
        "Sorry, I have no idea where to go then"
        ]
        return could_not_find[randrange(0, len(could_not_find))]


if __name__ == '__main__':
    sd = SpeechDiversifier()
    print sd.diversify_suggestion("test")
