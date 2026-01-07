#Importing Vital Libraries
import json
from pathlib import Path

#Important functions for table manipulations
def loadJSON(filepath):
  with open(filepath, "r") as f:
    return json.load(f)

def saveJSON(filepath, data):
  with open(filepath, "w") as f:
    json.dump(data, f, indent = 4)
