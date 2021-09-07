from Cards import deckOfCards
from Cards import Card
import random
class Game:
  def __init__(self):
    self.card = deckOfCards()
    random.shuffle(self.card)
    #self.money = round(money, 2)
    self.pCards = self.cardForEach(2)
    self.cCards = self.cardForEach(1)

  def getMoney(self):
    return self.money
  def getPCards(self):
    return self.pCards
  def getCCards(self):
    return self.cCards

  def cardForEach(self, num: int):
    c = []
    for i in range(num):
      c.append(self.card[0])
      self.card.pop(0)
    return c

  def drawCard(self,c:list):
    c.append(self.card[0])
    self.card.pop(0)
  
  def sumValue(self,c:list):
    value = 0
    ace = []
    for i in range(len(c)):
      if c[i].getIdentifyer() == 1:
        ace.append(c[i])
      else:
        value += c[i].getValue()
    for j in range(len(ace)):
      for k in range(2):
        if (value + ace[j].getValue().__getitem__(k + 1)) > 22:
          value += ace[j].getValue().__getitem__(k)
          break
        else:
          value += ace[j].getValue().__getitem__(k + 1)
          break
    return value

  def playGame(self):
    print("Blackjack!")
    #print("You have " + str(self.money) + " dollars")
    #self.bet = input("How much do you want to bet? ")
    self.pValue = self.sumValue(self.pCards)
    self.cValue = self.sumValue(self.cCards)
    pWin = False
    pBust = False
    cBust = False
    self.printGame()
    while(True):
      print("hit to draw another card or stay to pass")
      action = str(input("\n"))
      print()
      action.lower()
      if self.sumValue(self.pCards) == 21:
        pWin = True
        break
      elif(action.__eq__("stay")or action.__eq__("s")):
        self.pValue = self.sumValue(self.pCards)
        break
      elif(action.__eq__("hit") or action.__eq__("h")):
        self.drawCard(self.pCards)
        self.pValue = self.sumValue(self.pCards)
        self.printGame()
        if self.pValue > 21:
          print("You busted")
          pBust = True
          break
      else:
        print("Please enter hit or stay")

    while(pBust == False and not pWin):
      self.drawCard(self.cCards)
      self.cValue = self.sumValue(self.cCards)
      if self.cValue > 21:
        save = self.cCards[len(self.cCards) - 1]
        self.cCards.pop()
        if(self.sumValue(self.cCards) >= self.pValue or    ((21 - self.sumValue(self.cCards)) < (21 - self.cValue))):
          self.cValue = self.sumValue(self.cCards)
          break
        else:
          self.cCards.append(save)
          self.cValue = self.sumValue(self.cCards)
          cBust = True
          self.printGame()
          print("Dealer Busted")
          print("You Win")
          break
      if self.cValue == 21:
        break
    if(pWin):
      print("You Win")
    if(not pBust and not cBust):
      self.printGame()
    if self.pValue > self.cValue and not pBust:
      print("You Win")
    if self.cValue > self.pValue and not cBust:
      print("You Lost")
    if self.cValue == self.pValue:
      print("You tied")
      
  def printGame(self):
    print("Your cards: ")
    for i in range(len(self.pCards)):
      print(self.pCards[i])
    print("Total: " + str(self.pValue))
    print("~~~~~~~~~~~~~~~~~~")
    print("Dealer's cards: ")
    for j in range(len(self.cCards)):
      print(self.cCards[j])
    print("Total: " + str(self.sumValue(self.cCards)))

  def test(self):
    return None