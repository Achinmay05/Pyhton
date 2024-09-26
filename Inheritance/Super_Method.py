class Employee:
    def __init__(self):
        print("Constructor of Employee")
        
    a = 1
    
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2
    
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3
    
# o = Employee()
# print(o.a) #prints the a attribute
# print(o.b) #shows error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)