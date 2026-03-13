import json
import pathlib
import table_manipulation as t
import oop as o

test = (t.loadJSON(filepath = "./src/creatures.json"))
for i in range(len(test["faeries"])):
    if i % 2 != 0:
        print(test["faeries"][i])
