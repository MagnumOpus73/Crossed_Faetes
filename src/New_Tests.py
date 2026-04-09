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

Evolve_Test = o.InPlay_Faerie(attempt_F["name"], attempt_F["court"], attempt_F["hp"], attempt_F["attack"], attempt_F["defense"], attempt_F["speed"], attempt_F["canEvolve"], attempt_F["evolved"], attempt_F["movePool"], 10, 0)

Evolve_Test.Evolve()

Evolve_Test.playerDisplay()

print(len(test_Faeries["faeries"]))

print(len(t.loadJSON(filepath = "./src/creatures.json")["faeries"])/2)

NewMove = o.move(**o.getMove("Funeral Pyre"))

print(NewMove.getName())
