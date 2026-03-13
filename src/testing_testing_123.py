import json
import pathlib
import table_manipulation as t
import oop as o

test = (t.loadJSON(filepath = "./src/creatures.json"))
for i in test["faeries"]:
    print(test["faeries"][i]["name"])
