#Potentially necessary libraries/other functions
import json
import table_manipulation as t
import pathlib
import random as r


class Faerie:
  def __init__(self, name, court, hp, attack, defense, speed, canEvolve, evolved, movePool):
    self.Name = name
    self.Court = court
    self.baseHP = hp
    self.baseAttack = attack
    self.baseDefense = defense
    self.baseSpeed = speed
    self.canEvolve = canEvolve
    self.Evolved = evolved
    self.Movepool = movePool
#Function for later and for testing.  
  def display(self):
    print()
    print(self.Name)
    print(self.Court)
    print(self.baseHP)
    print(self.baseAttack)
    print(self.baseDefense)
    print(self.baseSpeed)
    print(self.Movepool)
    print()
    
#Split between the class for database use and the ones being used by the user and enemies.    
class InPlay_Faerie(Faerie):
  def __init__(self, name, court, hp, attack, defense, speed, canEvolve, evolved, movePool, level, killCount):
    Faerie.__init__(self, name, court, hp, attack, defense, speed, canEvolve, evolved, movePool)
    self.Level = level
    self.HP = round((((hp*2) + (level*10))/160)+(level * 10)+25)   #Turning base stats to actual stats via Mathematics.
    self.Attack = round((((attack * 2) + (level*10))/10) + (level*10) + 25)
    self.Defense = round((((defense * 2) + (level*10))/10) + (level*10) + 25)
    self.Speed = round((((speed * 2) + (level*10))/10) + (level*10) + 25)
    self.Kills = killCount
    self.currentHP = self.HP
    self.Fainted = False
    self.Poisoned = 0
    self.Burning = 0
    self.Withering = 0
    self.Regrowing = 0
    self.Protected = 1

  def getMovefromMovepool(self, index):
    print(self.Movepool)
    return self.Movepool[index]   

  def getAttack(self):
    return self.Attack
  
  def getDefense(self):
    return self.Defense
  
  def getSpeed(self):
    return self.Speed
  
  def getHP(self):
    return self.HP
  
  def Evolve(self):
    if self.canEvolve == "True" and self.Level >= 10:
      print("Can Evolve!!!")
      new_Faerie = (t.loadJSON(filepath = "./src/creatures.json"))
      for i in range(len(new_Faerie["faeries"])):
        if i % 2 != 0:
          if new_Faerie["faeries"][i]["name"] == self.Name:
            print(new_Faerie["faeries"][i+2]["name"])
            self.__init__(**new_Faerie["faeries"][i+2], level = self.Level, killCount = self.Kills)
            break
            
  def E_Evolve(self):
    if self.canEvolve == "True" and self.Level >= 10:
      new_Faerie = (t.loadJSON(filepath = "./src/creatures.json"))
      for i in range(len(new_Faerie["faeries"])):
        if i % 2 != 0:
          if new_Faerie["faeries"][i]["name"] == self.Name:
            self.__init__(**new_Faerie["faeries"][i+2], level = self.Level, killCount = self.Kills)
            break



  def takeDamage(self, damage):
    self.currentHP = round(self.currentHP - damage)
    if self.currentHP <= 0:
      self.Fainted = True
      self.currentHP = 0
      print(self.Name, "has fainted!")
    elif self.currentHP > self.HP:
      self.currentHP = self.HP


  def LevelUp(self):
    self.Kills += 1
    if self.Level < 10 and self.Kills == (self.Level * 2):
      self.Kills = 0
      self.Level = self.Level + 1
      self.Evolve()
      print("Your", self.Name, "levelled up!")
    else:
      print("Your", self.Name, "got a kill! Nice!")

  def getProtected(self):
    return self.Protected

  def playerDisplay(self):
    print(self.Name)
    print(self.Court)
    print(self.baseHP, self.HP)
    print(self.baseAttack, self.Attack)
    print(self.baseDefense, self.Defense)
    print(self.baseSpeed, self.Speed)
    print(self.Movepool)
  
  def opponentDisplay(self):
    print("Opponent's HP:", str(self.currentHP) + "/" + str(self.HP))
    print()

  def battleDisplay(self):
    print("Current HP:", str(self.currentHP) + "/" + str(self.HP))
    print(self.Movepool)
    print()

class JSON_Faeries:
  def __init__(self, file_path = "creatures.json"):
    self.filePath = pathlib.Path(file_path)
    self.data = t.loadJSON(pathlib.Path(file_path))

def displayJSON(self, file_path = "creatures.json"):
  print(self.data)
  

class move:
  def __init__(self, name, type, power, accuracy, protecting):
    self.Name = name
    self.Power = power
    self.Type = type
    self.Accuracy = accuracy
    self.Protecting = protecting
  
  def displayMove(self):
    if self.Type == "Attack":
      print(self.Name)
      print(self.Type)
      print("Power: " + str(self.Power))
      print("Accuracy: " + str(self.Accuracy))
    else:
      print(self.Name)
      print(self.Type)
      print("Accuracy: " + str(self.Accuracy))

  def getAccuracy(self):
    return self.Accuracy
      
  def getType(self):
    return self.Type

  def getPower(self):
    return self.Power
  
  def getName(self):
    return self.Name


class Entity:
  def __init__(self, name):
    self.Defeated = False
    self.Party = [None]*3
    self.Name = name
    self.ValidTeamMember = self.Party
    self.ValidTeamNumber = len(self.ValidTeamMember)

  def getParty(self):
    return self.Party

  def getPartyLength(self):
    length = len(self.Party)
    for i in self.Party:
      if i == None:
        length -= 1
    return length

  def FaerieDefeated(self):
    self.ValidTeamMember.pop(0)
    self.ValidTeamNumber -= 1


class Player(Entity):
  def __init__(self, name, item, bag):
    Entity.__init__(self, name)
    Player.equippedItem = item
    Player.Inventory = bag
    

class Player_File():
  def __init__(self, name, items):
    self.name = name
    self.items = items
  
  def getName(self):
    return self.name
  
  def getItems(self):
    return self.items

  def savePlayer(self):
    save_data = {
        "name": self.name,
        "items": self.items
    }
    print("Save successful!")
    return save_data


def calculate_damage(power, level, attack, enemy_defense, protection):
  return(round(((2 * level + 2) * power * (attack/enemy_defense)) * protection)/20)

def getFaerie(name):
  new_Faerie = (t.loadJSON(filepath = "./src/creatures.json"))
  for i in range(len(new_Faerie["faeries"])):
    if i % 2 != 0:
      if new_Faerie["faeries"][i]["name"] == name:
        return new_Faerie["faeries"][i]
      
def getMove(name):
  new_Move = (t.loadJSON(filepath = "./src/moves.json"))
  for i in range(len(new_Move["moves"])):
    if i % 2 != 0:
      if new_Move["moves"][i]["name"] == name:
        print(new_Move["moves"][i])
        new_Move = move(**new_Move["moves"][i])
        new_Move.displayMove()
        return new_Move
      else:
        print(new_Move["moves"][i])