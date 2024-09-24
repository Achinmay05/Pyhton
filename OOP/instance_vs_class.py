class Employee:
    language = "Python" #This is a class attribute.
    salary = 1200000
    
chinmay = Employee()
chinmay.language = "C++" #This is an object attribute or instance attribute.
print(chinmay.language, chinmay.salary)
