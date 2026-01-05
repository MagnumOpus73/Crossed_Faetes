class Faerie:
  def __init__(self, name, level, court, hp, attack, defense, speed):
    self.Name = name
    self.Level = level
    self.Court = court
    self.baseHP = hp
    self.baseAttack = attack
    self.baseDefense = defense
    self.baseSpeed = speed
    self.HP = round((((hp * 2) + level)/100) + level + 10)
    self.Attack = round((((attack * 2) + level)/100) + 5)
    self.Defense = round((((defense * 2) + level)/100) + 5)
    self.Speed = round(((speed * 2) + level)/100) + 5)
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


test1 = Faerie("TEST", 50, "NULL", 80, 80, 80, 80)
display(test1)
