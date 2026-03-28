import json
import pathlib
import table_manipulation as t
import oop as o

test = (t.loadJSON(filepath = "./src/creatures.json"))
for i in range(len(test["faeries"])):
    if i % 2 != 0:
        if test["faeries"][i]["name"] == "Pyree":
            print(test["faeries"][i])
            attempt = test["faeries"][i]



test_Faerie = o.InPlay_Faerie(attempt["name"], 1, attempt["court"], attempt["hp"], attempt["attack"], attempt["defense"], attempt["speed"], attempt["canEvolve"], 0, attempt["movePool"])

test_Faerie.display()

test_Faerie.takeDamage(20)

test_Faerie.battleDisplay()