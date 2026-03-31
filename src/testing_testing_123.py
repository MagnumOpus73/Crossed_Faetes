import json
import pathlib
import table_manipulation as t
import oop as o

test_Faeries = (t.loadJSON(filepath = "./src/creatures.json"))
for i in range(len(test_Faeries["faeries"])):
    if i % 2 != 0:
        if test_Faeries["faeries"][i]["name"] == "Pyree":
            print(test_Faeries["faeries"][i])
            attempt_F = test_Faeries["faeries"][i]

test_Moves = (t.loadJSON(filepath = "./src/moves.json"))
for i in range(len(test_Moves["moves"])):
    if i % 2 != 0:
        if test_Moves["moves"][i]["name"] == "TESTING-D":
            print(test_Moves["moves"][i])
            attempt_M = test_Moves["moves"][i]


test_Move = o.move(attempt_M["name"], attempt_M["type"], attempt_M["power"], attempt_M["accuracy"])

print(test_Move.getName())

print(attempt_F)

test_Faerie = o.InPlay_Faerie(attempt_F["name"], 1, attempt_F["court"], attempt_F["hp"], attempt_F["attack"], attempt_F["defense"], attempt_F["speed"], attempt_F["canEvolve"], 0, attempt_F["movePool"])

print(test_Faerie.Movepool)

test_Faerie.display()

test_Faerie.takeDamage(20)

test_Faerie.battleDisplay()

test_Faerie.playerDisplay()

test_FaeriesE = (t.loadJSON(filepath = "./src/creatures.json"))
for i in range(len(test_FaeriesE["faeries"])):
    if i % 2 != 0:
        if test_FaeriesE["faeries"][i]["name"] == "Rimekin":
            print(test_FaeriesE["faeries"][i])
            attempt_FE = test_FaeriesE["faeries"][i]

test_enemy = o.InPlay_Faerie(attempt_FE["name"], 1, attempt_FE["court"], attempt_FE["hp"], attempt_FE["attack"], attempt_FE["defense"], attempt_FE["speed"], attempt_FE["canEvolve"], 0, attempt_FE["movePool"])

test_Faerie.takeDamage(o.calculate_damage(test_Move.getPower(), test_Faerie.Level, test_Faerie.Attack, test_enemy.Defense))

test_Faerie.battleDisplay()
print()
test_enemy.battleDisplay()