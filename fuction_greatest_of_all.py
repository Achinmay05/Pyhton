a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))

def greatest(a, b, c):
    if(a > b and a > c):
        return a
    
    elif(b > a and b > c):
        return b
    
    elif(c > a and c > b):
        return c
    
    else:
        return 0
    
print(f"greatest number is {greatest(a, b, c)}")