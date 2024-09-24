class Employee:
    language = "Python" #This is a class attribute.
    salary = 1200000
    
    def getInfo(self):
        print(f"the language is {self.language}, and the salary is {self.salary}")
        
    def greet(self):
        print("Good Morning!")
        
    
chinmay = Employee()
chinmay.language = "C++" #This is an object attribute or instance attribute.
chinmay.getInfo() #this command is same as Employee.getInfo(chinmay)
chinmay.greet()  
