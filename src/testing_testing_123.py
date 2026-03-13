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



test_Faerie = o.Faerie(attempt["name"], attempt["court"], attempt["hp"], attempt["attack"], attempt["defense"], attempt["speed"], attempt["canEvolve"], attempt["movePool"])

test_Faerie.display()