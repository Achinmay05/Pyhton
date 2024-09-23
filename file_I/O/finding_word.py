with open("long.txt") as f:
    x = f.read()

if("python" in x):
    print("Found!")

else:
    print("Not Found!")