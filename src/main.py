#Importing necessary libraries and internal files
import oop as o
import battle as b
import random as r
import table_manipulation as t
from pathlib import Path
game_over = False
Opponent = o.Entity("Opoonent")
print("Main Menu, please input the number corresponding to the option you want to select:   ")
print()
print("1. New Game")
print("2. Load Game")
print("9. Exit Game")
valid = False
save_files = (t.loadJSON(filepath = "./src/save_files.json"))
Player = o.Player_File(**save_files)
print("Availiable Player:", Player.getName())
while valid == False:
    choice = input("Enter your choice: ")

    if choice == "1":
     name = input("What is your name? ")
     Player = o.Player_File(name, "[]")
     valid = True
    elif choice == "2":        
        print("Player loaded successfully.")
        valid = True
    elif choice == "9":
        print("Exiting game...")
        valid = True
    else:
        print("Invalid choice.")

while game_over == False:
    valid = False
    Player_Entity = o.Player(Player.getName(), Player.getItems(), "[]")
    print("What Faerie do you choose to start your adventure with? Pyree, Rimekin, Chither or Evergrow? ")
    while valid == False:
        run_begin = input()
        if run_begin == "Pyree" or run_begin == "Evergrow" or run_begin == "Chither" or run_begin == "Rimekin":
            Player_Faerie = o.InPlay_Faerie(**o.getFaerie(run_begin), level = 1, killCount = 0)
            Player_Entity.Party[0] = Player_Faerie
            valid = True
        else:
            print("Invalid first choice.")
        while game_over == False:
            Opponent.Party[0] = Opponent
            b.battle(Player_Entity, Player_Faerie, )
        

    
