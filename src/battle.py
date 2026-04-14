#Importing important methods from other programs within the main file.
import oop as o
import table_manipulation as t
import random as r

def attack(move_name, attacker, defender):
  move = o.getMove(move_name)
  move.displayMove()
  print(attacker.Name, "used", move.getName() + "!")
  if move.getAccuracy() >= r.randint(1, 100):
    if move.getType() == "Damage":
      damage = o.calculate_damage(move.getPower(), attacker.Level, attacker.Attack, defender.Defense, defender.Protected)
      print(damage)
      defender.takeDamage(damage)
      attacker.battleDisplay()
      defender.battleDisplay()
    else:
      if move_name == "Light Up":
        defender.Burning = 3
        print(defender.Name, "was burned!")
      elif move_name == "Glowing Wick":
        attacker.Protected = 0.6
      elif move_name == "Hot Coals":
        if r.randint(1,5) == 1:
          defender.Burning = 3
          print(defender.Name, "was burned!")
          defender.takeDamage(20, defender)
      elif move_name == "Accellerant":
        defender.takeDamage(o.calculate_damage((20*defender.Burning), attacker.Level, attacker.Attack, defender.Defense, defender.Protected), defender)
      elif move_name == "Combustible":
        if r.randint(1,2) == 1:
          defender.takeDamage(o.calculate_damage((85), attacker.Level, attacker.Attack, defender.Defense, defender.Protected), defender)
        else:
          attacker.takeDamage(o.calculate_damage((15), attacker.Level, attacker.Attack, defender.Defense, defender.Protected), attacker)
          print("The attack backfired!")
      elif move_name == "Enflame":
        defender.Burning = 4
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
  self.Protected = 1
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



def battle(Player, Player_Faerie, Opponent, opponent_Faerie):
  turn_count = 0
  start_of_turn(turn_count, Player_Faerie)
  start_of_turn(turn_count, opponent_Faerie)
  while opponent_Faerie.currentHP != 0 and Player_Faerie.currentHP != 0:
    start_of_turn(turn_count, Player_Faerie)
    start_of_turn(turn_count, opponent_Faerie)
    playerAction = 0
    while playerAction == 0:
      Player_Faerie.battleDisplay()
      print("Would you like to attack (A), attempt a contract(C), or forfeit your life(F)?")  
      playerAction = input()
      if playerAction == "A":
        valid = False
        while valid == False:
          print("Which move would you like to use? (Make sure your spelling is exact.)")
          move = input()
          try:
            move = o.getMove(move)
            valid = True
          except:
            print("Invalid move. Try again.")

      elif playerAction == "C":
        if len(Player.Party) >= 3:
          print("Your party is full! You cannot contract more Faeries.") 
        else:
          if r.randint(1, (100*(opponent_Faerie.currentHP/opponent_Faerie.HP))) <= 15:
            print("Contract successful!")
            Player.Party.append(opponent_Faerie)
            opponent_Faerie.playerDisplay()
            opponent_Faerie.currentHP = 0
      elif playerAction == "F":
        forfeit = True
        Player_Faerie.currentHP = 0
        Player.ValidTeamNumber = 0
        break
      else:
        print("Invalid input: Try Again.")
        playerAction = 0
    if opponent_Faerie.getSpeed() > Player_Faerie.getSpeed():
      print("The opponent strikes first!")
      attack(opponent_Faerie.Movepool[r.randint(0, 3)], opponent_Faerie, Player_Faerie)
      if Player_Faerie.currentHP != 0:
        attack(move, Player_Faerie, opponent_Faerie)
    elif opponent_Faerie.getSpeed() < Player_Faerie.getSpeed():
      print("You strike first!")
      attack(move, Player_Faerie, opponent_Faerie)
      if opponent_Faerie.currentHP != 0:
        attack(opponent_Faerie.Movepool[r.randint(0, 3)], opponent_Faerie, Player_Faerie)
    elif opponent_Faerie.getSpeed() == Player_Faerie.getSpeed():
      if r.randint(1, 2) == 1:
        print("The opponent strikes first!")
        attack(opponent_Faerie.Movepool[r.randint(0, 3)], opponent_Faerie, Player_Faerie)
        if Player_Faerie.currentHP != 0:
          attack(move, Player_Faerie, opponent_Faerie)
      else:
        print("You strike first!")
        attack(move, Player_Faerie, opponent_Faerie)
        if opponent_Faerie.currentHP != 0:
          attack(opponent_Faerie.Movepool[r.randint(0, 3)], opponent_Faerie, Player_Faerie)
    opponent_Faerie.battleDisplay()
    Player_Faerie.battleDisplay()
    if o.Player.currentHP == 0:
      if o.Player.ValidTeamNumber == 0:
        if forfeit == False:
          print("Loss")
        else:
          print("You forfeited your life. Game Over.")
      elif o.Player.ValidTeamNumber > 0:
        print("Next up!")

  if opponent_Faerie.currentHP == 0:
    o.InPlay_Faerie.LevelUp(Player_Faerie)
    if Opponent.ValidTeamNumber == 0:
      print("Win.")
    elif Opponent.ValidTeamNumber > 0:
      print("Next enemy.")





attack("Spark", Player_Faerie, getOpponent(Player_Faerie))
