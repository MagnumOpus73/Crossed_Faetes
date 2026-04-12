#Importing important methods from other programs within the main file.
import oop as o
import table_manipulation as t
import random as r

def attack(move_name, attacker, defender):
  move = o.getMove(move_name)
  print(attacker.Name, "used", move["name"] + "!")
  if move["accuracy"] >= r.randint(1, 100):
    if move["type"] == "Damage":
      damage = o.calculate_damage(move["power"], attacker.Level, attacker.Attack, defender.Defense, 1)
      print(damage)
      defender.takeDamage(damage)
      attacker.battleDisplay()
      defender.battleDisplay()
    else:
      print("Not done yet. - Need to make all status moves do their unique effects.")
  else:
    print("But it missed!")


Test_Player = o.Player("Test_Player", "NULL", [])


Player_Faerie = o.InPlay_Faerie(**o.getFaerie("Sprire"), level = 11, killCount = 0)


playerAction = 0

def getOpponent(player):
  opponent = (t.loadJSON(filepath = "./src/creatures.json"))
  repeat = True
  while repeat == True:
    randomID = r.randint(1, (int(len(t.loadJSON(filepath = "./src/creatures.json")["faeries"])/2)))
    randomID = (randomID * 2) - 1
    print(randomID)
    opponent_Faerie = opponent["faeries"][randomID]
    if player.Level != 1:
      opponent_Faerie = o.InPlay_Faerie(opponent_Faerie["name"], opponent_Faerie["court"], opponent_Faerie["hp"], opponent_Faerie["attack"], opponent_Faerie["defense"], opponent_Faerie["speed"], opponent_Faerie["canEvolve"], opponent_Faerie["evolved"], opponent_Faerie["movePool"], level = r.randint((player.Level - 1), (player.Level + 1)), killCount = 0)
    else:
      opponent_Faerie = o.InPlay_Faerie(opponent_Faerie["name"], opponent_Faerie["court"], opponent_Faerie["hp"], opponent_Faerie["attack"], opponent_Faerie["defense"], opponent_Faerie["speed"], opponent_Faerie["canEvolve"], opponent_Faerie["evolved"], opponent_Faerie["movePool"], level = 1, killCount = 0)
    
    if opponent_Faerie.Evolved == "True":
      print("Evolved.")
    else:
      print("Unevolved.")
      break
  if r.randint(1, 2) == 1:
    opponent_Faerie.E_Evolve()
  else:
    pass
  print(opponent_Faerie.Name, "is summoned to the field!")
  opponent_Faerie.playerDisplay()
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



def battle(Player_Faerie, opponent):
  turn_count = 0
  start_of_turn(turn_count, Player_Faerie)
  start_of_turn(turn_count, opponent)
  while opponent.currentHealth != 0 and Player_Faerie.currentHealth != 0:
    start_of_turn(turn_count)
    while playerAction == 0:
      Player_Faerie.battleDisplay()
      playerAction = input("Would you like to attack (A), use an item(I), or flee(F)?").upper  
      if playerAction == "A":
        valid = False
        while valid == False:
          print("Which move would you like to use? (Make sure your spelling is exact.)")
          move = input()
          try:
            o.getMove(move), Player_Faerie, opponent
            valid = True
          except:
            print("Invalid move. Try again.")

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





attack("Spark", Player_Faerie, getOpponent(Player_Faerie))
