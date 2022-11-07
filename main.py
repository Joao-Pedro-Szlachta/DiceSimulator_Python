# Dice SImulator
# It simulates a dice, it generates a value from 1 to 6

import random
import PySimpleGUI as sg


class DiceSimulator:

  def __init__(self):
    self.min_value = 1
    self.max_value = 6

    self.layout = [[sg.Text('Would you like to toss the dice')],
                   [sg.Button('Yes'), sg.Button('Not')]]

  def initiate(self):
    self.window = sg.Window('Dice Simulator', self.layout)
    self.events, self.values = self.window.Read()

    try:
      if (self.events == 'Yes'):
        self.TossTheDice()
      elif (self.events == 'Not'):
        print('We appreciate your participation')
      else:
        print('Please, write "yes / y" or "not / n"')
    except:
      print("There was a problem in your answer")

  def TossTheDice(self):
    print(random.randint(self.min_value, self.max_value))


simulator = DiceSimulator()
simulator.initiate()
