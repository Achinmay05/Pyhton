word = "Donkey"

with open("first.txt", "r") as f:
    content = f.read()
    
contentNew = content.replace("Donkey", "######")

with open("first.txt", "w") as f:
    f.write(contentNew)
    