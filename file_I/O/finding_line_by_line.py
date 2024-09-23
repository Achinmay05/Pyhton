with open("long.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Found in line: {lineno}")
        break
    lineno += 1
    
else:
    print("Not Found!")