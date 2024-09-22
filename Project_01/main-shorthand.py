# 1 for snake 
# -1 for water
# 0 for gun
import random
computer = random.choice([-1, 0, 1])
youstr = input("enter your choice : ")

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
   -1: "Water",
    0: "Gun"    
}

you = youDict[youstr]

print(f"Computer chose {reverseDict[computer]}")
print(f"You chose {reverseDict[you]}")

if(computer == you):
    print("Draw!")
    
else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("You Lose")
        
    else:
        print("You Win")