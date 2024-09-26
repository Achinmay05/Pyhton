class Calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"the square is: {self.n * self.n}")
        
    def cube(self):
        print(f"the cube is: {self.n * self.n * self.n}")
        
    def squareroot(self):
        print(f"The square root is: {self.n ** (1/2)}")
        
    @staticmethod
    def greet():
        print("Hello User!")
        
a = Calculator(16)
a.square()
a.cube()
a.squareroot()
a.greet()