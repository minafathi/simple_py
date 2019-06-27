class simple_math:

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def plusme(self):
        result = self.x + self.y
        return result

    def minesme(self):
        result = self.x - self.y
        return result
    
    def multiplicationme(self):
        result = self.x * self.y
        return result

    def divisionme(self):
        result = self.x / self.y
        return result

my_var = simple_math(9, 3)
print(my_var.divisionme())
print(my_var.plusme())
