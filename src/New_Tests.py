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

Evolve_Test = o.InPlay_Faerie(attempt_F["name"], 11, attempt_F["court"], attempt_F["hp"], attempt_F["attack"], attempt_F["defense"], attempt_F["speed"], attempt_F["canEvolve"], 0, attempt_F["movePool"])

Evolve_Test.Evolve()

Evolve_Test.display()