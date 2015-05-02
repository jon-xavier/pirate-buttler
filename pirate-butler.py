responses ={}

def askpiratequestions():
  questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}
  
  for question in questions:
    response = raw_input("{} Enter Yes or No: " .format(questions.get(question),))
    if response == "Yes" or response =="yes" or response == "y" or response =="Y":
      response = True
    elif response == "No" or response == "no" or response == "n" or response == "N":
      response = False
      ## ask all the questions in the questions dictionary, then set a response to true or false
    responses[question] = response
    ## Create a key and value in the dictionary responses where the value is equal to response

def makepiratedrink():
  Drink = []
  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
  for response in responses:
    if response is True
    drink.append(random.choice(ingredients{response}))
    
    return Drink
    
if __name__ == "__main__":
  askpiratequestions()
  makepiratedrink()
  print Drink

