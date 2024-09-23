import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 63)
    
    with open("high_Score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"your score: {score}")
    if(score > hiscore):
        with open("high_Score.txt", "w") as f:
            f.write(str(score))
            
    return score

game()
    