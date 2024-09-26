class Programmer:
    company = "Microsoft"
    def  __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = Programmer("Chinmay", 1200000, 482002)
print(p.name, p.salary, p.pin, p.company)
g = Programmer("Ghidorah", 1200000, 482002)
print(g.name, g.salary, g.pin, g.company)
        