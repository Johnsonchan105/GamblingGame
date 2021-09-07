class Card:
  def __init__(self, values, colors):
    v = ''
    value = None
    if values == 1:
      v = 'Ace of '
      value = [1, 11]
    elif values == 11:
      v = 'Jack of '
      value = 10
    elif values == 12:
      v = 'Queen of '
      value = 10
    elif values == 13:
      v = 'King of '
      value = 10
    else:
      v = str(values) + ' of '
      value = values
    self.num = v
    self.value = value
    self.color = colors
    self.identifyer = values
  def getValue(self):
    return self.value
  def getIdentifyer(self):
    return self.identifyer
  def __str__(self):
    return self.num + self.color
def deckOfCards():
  color = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
  cards = [Card(values, colors) for values in range(1, 14) for colors in color] 
  return cards