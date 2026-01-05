#Importing necessary libraries
import json
from pathlib import Path

#Functions useful for handling JSON Files.
def loadJSON(filepath):
  with open(filepath, "r") as f:
    return json.load(f)

def saveJSON(filepath, data):
  with open(filepath, "w") as f:
    json.dump(data, f, indent = 4)

#Creation of monster object.
class Faerie:
  def __init__(self, name, level, court, hp, attack, defense, speed, canEvolve):
    self.Name = name
    self.Level = level
    self.Court = court
    self.baseHP = hp
    self.baseAttack = attack
    self.baseDefense = defense
    self.baseSpeed = speed
    self.canEvolve = canEvolve
    self.HP = round((((hp * 2) + level)/160) + (level * 2) + 25)   #Turning base stats to actual stats via Mathematics.
    self.Attack = round((((attack * 2) + level)/10) + level + 25)
    self.Defense = round((((defense * 2) + level)/10) + level + 25)
    self.Speed = round((((speed * 2) + level)/10) + level + 25)
#Function for later and for testing.  
  def display(self):
    print(self.Name)
    print(self.Level)
    print(self.Court)
    print(self.baseHP)
    print(self.HP)
    print(self.baseAttack)
    print(self.Attack)
    print(self.baseDefense)
    print(self.Defense)
    print(self.baseSpeed)
    print(self.Speed)

#Actual testing. How statlines appear when going through the formulas.
test1 = Faerie("TEST", 1, "NULL", 80, 80, 80, 80, "False")
test2 = Faerie("TEST", 50, "NULL", 80, 80, 80, 80, "False")
test3 = Faerie("TEST", 100, "NULL", 80, 80, 80, 80, "False")
Faerie.display(test1)
print()
Faerie.display(test2)
print()
Faerie.display(test3)
