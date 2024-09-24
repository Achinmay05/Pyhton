class Employee:
    language = "Python" #This is a class attribute.
    salary = 1200000
    
chinmay = Employee()
chinmay.name = "Chinmay Awasthi" #This is an object attribute or instance attribute.
print(chinmay.name, chinmay.language, chinmay.salary)

# here name is object attribute or instance attribute and language and salary are class attributes as they directly belongs to the class.