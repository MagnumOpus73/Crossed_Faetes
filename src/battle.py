#Importing important methods from other programs within the main file.
import oop as o
import table_manipulation as t
import random as r

def attack(move_name, attacker, defender):
  move = o.getMove(move_name)
  print(attacker.Name, "used", move.getName() + "!")
  if move.getAccuracy() >= r.randint(1, 100):
    if move.getType() == "Damage":
      defender.takeDamage(o.calculate_damage(move.getPower(), attacker.getLevel(), attacker.getAttack(), defender.getDefense()))
    else:
      print("Not done yet. - Need to make all status moves do their unique effects.")
  else:
    print("But it missed!")


Test_Player = o.Player("Test_Player", "NULL", [])


Player_Faerie = o.getFaerie("Pyree")


playerAction = 0

def getOpponent():
  opponent = (t.loadJSON(filepath = "./src/creatures.json"))
  randomID = r.randint(1, (int(len(t.loadJSON(filepath = "./src/creatures.json")["faeries"])/2)))
  randomID = (randomID * 2) - 1
  print(randomID)
  opponent_Faerie = opponent["faeries"][randomID]
  opponent_Faerie = o.InPlay_Faerie(opponent_Faerie["name"], opponent_Faerie["court"], opponent_Faerie["hp"], opponent_Faerie["attack"], opponent_Faerie["defense"], opponent_Faerie["speed"], opponent_Faerie["canEvolve"], opponent_Faerie["evolved"], opponent_Faerie["movePool"], level = 1, killCount = 0)
  opponent_Faerie.display()
  return opponent_Faerie



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




getOpponent()

attack("Funeral Pyre", Player_Faerie, getOpponent())