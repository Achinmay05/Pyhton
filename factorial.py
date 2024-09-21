a = int(input("enter the number : "))
fact = 1
i = 1
# while(i <= a):
#     fact *= i
#     i += 1
    
# print(f"factorial is : {fact}")

for i in range(1, a + 1):
    fact = fact * i
    
print(f"factorial is {fact}")