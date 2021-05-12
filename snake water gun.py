"This is a game of rock paper scissor using random module"""
import random
name=input("Please Enter your name")
n=0 #counter for number of games
cu=0#counter for wins of user
cp=0#counter for wins of computer
while n<5:
    choose=input("Please type your choice:\n"
               "1.Rock\n2.Paper\n3.Scissor")
    L=["Rock","Paper","Scissor"]
    choose1 = choose.capitalize()
    comp=random.choice(L)
    if choose1 == "Rock":
        if comp == choose1:
            print(f"Match is draw::{choose1} vs {comp} ")
        elif comp == "Scissor":
            print(f"You won ::{choose1} vs {comp}")
            cu+=1
        elif comp == "Paper":
            print(f"You Lost ::{choose1} vs {comp}")
            cp+=1
    if choose1 == "Paper":
        if comp == choose1:
            print(f"Match is draw::{choose1} vs {comp} ")
        elif comp == "Scissor":
            print(f"You Lost ::{choose1} vs {comp}")
            cp+=1
        elif comp == "Rock":
            print(f"You Won ::{choose1} vs {comp}")
            
    if choose1 == "Scissor":
        if comp == choose1:
            print(f"Match is draw::{choose1} vs {comp} ")
        elif comp == "Paper":
            print(f"You won ::{choose1} vs {comp}")
            cu+=1
        elif comp == "Rock":
            print(f"You Lost ::{choose1} vs {comp}")
            
    n+=1
