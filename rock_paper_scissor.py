import random
print("Welcome to Rock, Paper,Scissor")

user=input("Enter your name!")

game=["rock","paper","scissor"]
Computer=random.choice(game)

print(f"Hello! {user.title()}, ready to play?")

choose=int(input("Choose match type 3 or 5:"))

print(" "*60)

for i in range(1,choose+1):
    print(f"Round {i} of best of {choose}")
    user_choic=input("Choose rock, paper or scissor:")
    print(f"{user.title()} choose, {user_choic}")
    print(f"Computer choose,{Computer}")

    if user_choic=="rock" and Computer== "scissor":
        print(f"{user.title()} Wins")
        
        print(f"Score- computer:0, {user}:1")
    elif user_choic=="rock" and Computer== "paper":
        
        print("Computer Wins")
        print(f"Score- {user}:0, Computer:1")
    elif user_choic=="paper" and Computer== "scissor":
        print("Computer Wins")
        print(f"Score- {user}:0, Computer:1")    
    elif user_choic=="paper" and Computer== "rock":
        print(f"{user.title()} Wins")
        print(f"Score- computer:0, {user}:1")
    elif user_choic=="scissor" and Computer== "rock":
        print("Computer Wins")
        print(f"Score- {user}:0, Computer:1")
    elif user_choic=="scissor" and Computer== "paper":
        print(f"{user.title()} Wins")
        print(f"Score- Computer:0, {user}:1")
    elif user_choic==Computer:
        print("Game Draw")
    
    print(" "*50)