#Importing important methods from other programs within the main file.
import oop as o
import table_manipulation as t
import random as r

def attack(move_used, attacker, defender):
  move_used.displayMove()
  print(attacker.Name, "used", move_used.getName() + "!")
  if move_used.getAccuracy() >= r.randint(1, 100):
    if move_used.getType() == "Damage":
      damage = o.calculate_damage(move_used.getPower(), attacker.Level, attacker.Attack, defender.Defense, defender.Protected)
      print(damage)
      defender.takeDamage(damage)
      attacker.battleDisplay()
      defender.battleDisplay()
    else:
      if move_used.Name == "Light Up":
        defender.Burning = 3
        print(defender.Name, "was burned!")
      elif move_used.Name == "Glowing Wick":
        attacker.Protected = 0.6
      elif move_used.Name == "Hot Coals":
        if r.randint(1,5) == 1:
          defender.Burning = 3
          print(defender.Name, "was burned!")
          defender.takeDamage(20)
      elif move_used.Name == "Accellerant":
        defender.takeDamage(o.calculate_damage((20*defender.Burning), attacker.Level, attacker.Attack, defender.Defense, defender.Protected), defender)
      elif move_used.Name == "Combustible":
        if r.randint(1,2) == 1:
          defender.takeDamage(o.calculate_damage((85), attacker.Level, attacker.Attack, defender.Defense, defender.Protected), defender)
        else:
          attacker.takeDamage(o.calculate_damage((15), attacker.Level, attacker.Attack, defender.Defense, defender.Protected), attacker)
          print("The attack backfired!")
      elif move_used.Name == "Enflame":
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

def opponentDisplay(opponent_Faerie):
  print("Opponent's HP: ", opponent_Faerie.currentHP)

def start_of_turn(turn_count, self):
  if self.currentHP == None:
    self.currentHP = 0
  turn_count += 0.5
  print(turn_count)
  if turn_count % 1 == 0:
    self.opponentDisplay()
  else:
    self.battleDisplay()
  self.Protected = 1
  if self.Burning > 0:
    self.currentHP = self.takeDamage(round(1/8 * round(self.currentHP)))
    self.Burning -= 1
  elif self.Poisoned > 0:
    self.currentHP = self.takeDamage((1/16 * self.currentHP * self.Poisoned))
    self.Poisoned -= 1
  elif self.Regrowing > 0:
    self.currentHP = self.takeDamage((-1 * (1/8 * self.currentHP)))
    self.Regrowing -= 1
  elif self.Withering > 0:
    self.Withering -= 1
    if self.Withering > 0:
      print("You see your monster continue to wither away. ", self.Withering + "turns remaining.")
    else:
      self.currentHP = 0
  return turn_count



def battle(Player, Player_Faerie, Opponent, opponent_Faerie, game_over, Player_File):
  turn_count = 0
  forfeit = False
  while opponent_Faerie.currentHP != 0 and Player_Faerie.currentHP != 0:
    turn_count = start_of_turn(turn_count, Player_Faerie)
    turn_count = start_of_turn(turn_count, opponent_Faerie)
    enemy_move = opponent_Faerie.getMovefromMovepool(r.randint(0,3))
    enemy_action = o.getMove(enemy_move)
    print(enemy_move)
    playerAction = 0
    while playerAction == 0:
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
        if move.Protecting == "True":
          print("You protect yourself!")
          attack(move, Player_Faerie, opponent_Faerie)
          attack(enemy_action, opponent_Faerie, Player_Faerie)
        elif enemy_action.Protecting == "True":
          print("The enemy protects themself!")
          attack(enemy_action, opponent_Faerie, Player_Faerie)
          attack(move, Player_Faerie, opponent_Faerie)
        else:
          if opponent_Faerie.getSpeed() > Player_Faerie.getSpeed():
            print("The opponent strikes first!")
            attack(enemy_action, opponent_Faerie, Player_Faerie)
            if Player_Faerie.currentHP != 0:
              attack(move, Player_Faerie, opponent_Faerie)
          elif opponent_Faerie.getSpeed() < Player_Faerie.getSpeed():
            print("You strike first!")
            attack(move, Player_Faerie, opponent_Faerie)
            if opponent_Faerie.currentHP != 0:
              attack(enemy_action, opponent_Faerie, Player_Faerie)
          elif opponent_Faerie.getSpeed() == Player_Faerie.getSpeed():
            if r.randint(1, 2) == 1:
              print("The opponent strikes first!")
              attack(enemy_action, opponent_Faerie, Player_Faerie)
              if Player_Faerie.currentHP != 0:
                attack(move, Player_Faerie, opponent_Faerie)
          else:
            print("You strike first!")
            attack(move, Player_Faerie, opponent_Faerie)
            if opponent_Faerie.currentHP != 0:
              attack(enemy_action, opponent_Faerie, Player_Faerie)
      elif playerAction == "C":
        attack(enemy_action, opponent_Faerie, Player_Faerie)
        if Player.getPartyLength() >= 3:
          print("Your party is full! You cannot contract more Faeries.") 
        else:
          if r.randint(1, (round(100*(opponent_Faerie.currentHP/opponent_Faerie.HP)))) <= 20:
            print("Contract successful!")
            opponent_Faerie.currentHP = opponent_Faerie.HP
            Player.Party.append(opponent_Faerie)
            opponent_Faerie.playerDisplay()
            opponent_Faerie.currentHP = 0
          else:
            print("Contract Unsuccessful.")
      elif playerAction == "F":
        forfeit = True
        Player_Faerie.currentHP = 0
        Player.ValidTeamNumber = 0
        break
      else:
        print("Invalid input: Try Again.")
        playerAction = 0
    
    opponent_Faerie.opponentDisplay()
    Player_Faerie.battleDisplay()
    Player.getValidTeamNumber()
    if Player_Faerie.currentHP == 0:
      Player.FaerieDefeated()
      if Player.ValidTeamNumber > 0:
        print("Next up!")
        Player_Faerie = Player.Party[0]
        pass
      elif Player.ValidTeamNumber == 0:
        game_over = True
        if forfeit == False:
          print("Loss")
        else:
          print("You forfeited your life. Game Over.")

  if opponent_Faerie.currentHP == 0:
    Player_Faerie.LevelUp()
    if Opponent.ValidTeamNumber == 0:
      print("Win.")
    elif Opponent.ValidTeamNumber > 0:
      print("Next enemy.")
      print(Player.getParty())
  Player_File.savePlayer()
  print(game_over)
  print()
  print()
  return game_over