playerAction = 0

def damage(power, level, attack, enemy_defense):
  return(((2*level + 2) * power * (attack/enemy_defense))

def start_of_turn(turn_count):
  turn_count += 1
  
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


