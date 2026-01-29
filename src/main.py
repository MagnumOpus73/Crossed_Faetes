

#Importing necessary libraries and internal files
import oop

import json
from pathlib import Path

#Functions useful for handling JSON Files.
def loadJSON(filepath):
  with open(filepath, "r") as f:
    return json.load(f)

def saveJSON(filepath, data):
  with open(filepath, "w") as f:
    json.dump(data, f, indent = 4)

