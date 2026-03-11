#Importing important methods from other programs within the main file.
from . import oop as o
from . import table_manipulation as t

Test_Player = o.Player("Test_Player", "NULL", [])


Player_Faerie = o.InPlay_Faerie()

playerAction = 0

def damage(power, level, attack, enemy_defense):
  return((2 * (level * 20) + 2) * power * (attack/enemy_defense))

def start_of_turn(turn_count, self):
  turn_count += 0.5
  if self.Burning > 0:
    self.currentHP = o.takeDamage((1/8 * self.currentHP), self)
    self.Burning -= 1
  elif self.Poisoned > 0:
    self.currentHP = o.takeDamage((1/16 * self.currentHP * self.Poisoned), self)
    self.Poisoned -= 1
  elif self.Regrowing > 0:
    self.currentHP = o.takeDamage((-1 * (1/8 * self.currentHP), self))
    self.Regrowing -= 1
  elif self.Withering > 0:
    self.Withering -= 1
    if self.Withering > 0:
      print("You see your monster continue to wither away. ", self.Withering + "turns remaining.")
    else:
      self.currentHP = 0
  return turn_count



def battle():
  turn_count = 0
  while o.opponent.currentHealth != 0 and o.player.currentHealth != 0:
    start_of_turn(turn_count)
    while playerAction == 0:
      playerAction = input("Would you like to attack (A), use an item(I), or flee(F)?").upper  
      if playerAction == "A":
        print("Not done yet.")
      elif playerAction == "I":
        print("Not done yet.")
      elif playerAction == "F":
        print("Not done yet.")
      else:
        print("Invalid input: Try Again.")
        playerAction = 0
  if o.Player.currentHealth == 0:
    if o.Player.ValidTeamNumber == 0:
      print("Loss")
    elif o.Player.ValidTeamNumber > 0:
      print("Next up!")

  if o.Opponent.currentHealth == 0:
    o.InPlay_Faerie.LevelUp(Player_Faerie)
    if o.Opponent.ValidTeamNumber == 0:
      print("Win.")
    elif o.Opponent.ValidTeamNumber > 0:
      print("Next enemy.")
