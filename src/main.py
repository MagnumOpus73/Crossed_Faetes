#Importing necessary libraries and internal files
import oop as o
import battle as b
import random as r
import table_manipulation as t
from pathlib import Path

print("Main Menu, please input the number corresponding to the option you want to select:   ")
print()
print("1. New Game")
print("2. Load Game")
print("9. Exit Game")
valid = False
save_files = (t.loadJSON(filepath = "./src/save_files.json"))
print(save_files)
while valid == False:

    choice = input("Enter your choice: ")

    if choice == "1":
     name = input("What is your name? ")
     Player = o.Player_File(name, "[]")
     valid = True
    elif choice == "2":
        name = input("What is your name? ")
        try:
            with open("save_files.json", "r") as f:
                for i in range(len(["save_files"])):

                    if t.loadJSON(f)["save_files"][i]["name"] == name:
                        Player = o.Player_File(**t.loadJSON(f)["save_files"][i])        
                        print("Player loaded successfully.")
                        valid = True
        except:
            print("Player not found.")
    elif choice == "9":
        print("Exiting game...")
        valid = True
    else:
        print("Invalid choice.")
