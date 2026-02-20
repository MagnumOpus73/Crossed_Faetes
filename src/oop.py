#Potentially necessary libraries/other functions
import json
import src.table_manipulation
import pathlib from Path


class Faerie:
  def __init__(self, name, level, court, hp, attack, defense, speed, canEvolve, movePool):
    self.Name = name
    self.Court = court
    self.baseHP = hp
    self.baseAttack = attack
    self.baseDefense = defense
    self.baseSpeed = speed
    self.canEvolve = canEvolve
    self.HP = round((((hp * 2) + (level*20))/160) + (level * 20) + 25)   #Turning base stats to actual stats via Mathematics.
    self.Attack = round((((attack * 2) + (level*20))/10) + (level*20) + 25)
    self.Defense = round((((defense * 2) + (level*20))/10) + (level*20) + 25)
    self.Speed = round((((speed * 2) + (level*20))/10) + (level*20) + 25)
    self.Movepool = []
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
    
#Split between the class for database use and the ones being used by the user and enemies.    
class InPlay_Faerie(Faerie):
  def __init__(self, name, level, court, hp, attack, defense, speed, canEvolve, killCount, movePool):
    Faerie.__init__(self, name, level, court, hp, attack, defense, speed, canEvolve, movePool)
    self.Level = level
    self.Kills = killCount
    self.currentHP = self.HP
    self.Fainted = False
    self.Poisoned = 0
    self.Burning = 0
    self.Withering = 0
    self.Regrowing = 0    

  def takeDamage(damage, self):
    self.currentHP = self.currentHP - damage
    if self.currentHP <= 0:
      self.Fainted = True
    elif self.currentHP > self.HP:
      self.currentHP = self.HP

  def LevelUp(self):
    self.Kills += 1
    if self.Level < 5 and self.Kills == (self.Level * 5):
      self.Kills = 0
      self.Level = self.Level + 1
      print("Your", self.Name, "levelled up!")
    else:
      print("Your", self.Name, "got a kill! Nice!")


class JSON_Faeries:
  def __init__(self, file_path = "monsters.json"):
    self.filePath = Path(file_path)
    self.data = load_json(self.filePath)

def display(self, file_path = "monsters.json"):
  print(self.data)
  


class Entity:
  def __init__(self, name):
    self.Defeated = False
    self.Party = [NULL]*6
    self.Name = name
    self.ValidTeamMember = self.Party
    self.ValidTeamNumber = self.ValidTeamMember.count()

  def FaerieDefeated(self):
    self.ValidTeamMember.pop(0)
    self.ValidTeamNumber -= 1

class Player(Entity):
  def __init__(self, name, item, bag):
    Entity.__init__(self, name)
    Player.equippedItem = item
    Player.Inventory = bag
    


#Actual testing. How statlines appear when going through the formulas.
test1 = InPlay_Faerie("TEST", 1, "NULL", 80, 80, 80, 80, "False", 0, [])
test2 = InPlay_Faerie("TEST", 2, "NULL", 80, 80, 80, 80, "False", 0, [])
test3 = InPlay_Faerie("TEST", 5, "NULL", 80, 80, 80, 80, "False", 0, [])
InPlay_Faerie.display(test1)
print()
InPlay_Faerie.display(test2)
print()
InPlay_Faerie.display(test3)
