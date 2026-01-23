class Faerie:
  def __init__(self, name, level, court, hp, attack, defense, speed, canEvolve):
    self.Name = name
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
    
#Split between the class for database use and the ones being used by the user and enemies.    
class InPlay_Faerie(Faerie):
  def __init__(self, name, level, court, hp, attack, defense, speed, canEvolve, level):
    Faerie.__init__(self, name, level, court, hp, attack, defense, speed, canEvolve)
    self.Level = level
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

  def

#Actual testing. How statlines appear when going through the formulas.
test1 = InPlay_Faerie("TEST", 1, "NULL", 80, 80, 80, 80, "False")
test2 = InPlay_Faerie("TEST", 50, "NULL", 80, 80, 80, 80, "False")
test3 = InPlay_Faerie("TEST", 100, "NULL", 80, 80, 80, 80, "False")
InPlay_Faerie.display(test1)
print()
InPlay_Faerie.display(test2)
print()
InPlay_Faerie.display(test3)
