#Importing important methods from other programs within the main file.
import src.oop
import src.table_manipulation

Test_Player = Player("Test_Player", "NULL", [])


Player_Faerie = InPlay_Faerie()



playerAction = 0

def damage(power, level, attack, enemy_defense):
  return(((2 * (level * 20) + 2) * power * (attack/enemy_defense))

def start_of_turn(turn_count, self):
  turn_count += 0.5
  if self.Burning > 0:
    self.currentHP = takeDamage((1/8 * self.currentHP), self)
    self.Burning -= 1
  elif self.Poisoned > 0:
    self.currentHP = takeDamage((1/16 * self.currentHP * self.Poisoned), self)
    self.Poisoned -= 1
  elif self.Regrowing > 0:
    self.currentHP = takeDamage((-1 * (1/8 * self.currentHP), self))
    self.Regrowing -= 1
  elif self.Withering > 0:
    self.Withering -= 1
     if self.Withering > 0:
       print("You see your monster continue to wither away. ", self.Withering + "turns remaining.")
     else:
       self.currentHP = 0
    
  return turn_count




while opponent.currentHealth != 0 and player.currentHealth != 0:
  start_of_turn(turn_count)
  while playerAction == 0:
    playerAction = input("Would you like to attack (A), use an item(I), or flee(F)?").upper
    if playerAction == "A":

    elif playerAction == "I":

    elif playerAction == "F":

    else:
      print("Invalid input: Try Again.")
      playerAction = 0
if Player.currentHealth == 0:
  if Player.ValidTeamNumber == 0:
    #Player Loses
  elif Player.ValidTeamNumber > 0:
    #Player sends out next member.

if Opponent.currentHealth == 0:
  InPlay_Faerie.LevelUp(Player_Faerie)
  if Opponent.ValidTeamNumber == 0:
    #Player Wins.
  elif Opponent.ValidTeamNumber > 0:
    #Opponent sends out next member.

