with open("first.txt") as f:
    data = (f.read())
    
x = data.find("vibhu")

if(x > 0):
    print("found")
    
else:
    print("not found")