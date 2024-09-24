class Employee:
    language = "Python" #This is a class attribute.
    salary = 1200000
    
    def getInfo(self):
        print(f"the language is {self.language}, and the salary is {self.salary}")
        
    def __init__(self, name, salary, language): #dunder method which is automatically called when a new object is created.
        self.name = name
        self.salary = salary
        self.language = language
        print("creating an object")
        
    @staticmethod    
    def greet():
        print("Good Morning!")
        
    
chinmay = Employee("Chinmay", "6300000", "C++")
# chinmay.language = "C++" #This is an object attribute or instance attribute.
# chinmay.getInfo() #this command is same as Employee.getInfo(chinmay)
# chinmay.greet()  
print(chinmay.name, chinmay.language, chinmay.salary)
