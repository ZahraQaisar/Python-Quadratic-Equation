import math

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def display(self):
        print('a:',self.a, 'b:', self.b, 'c:', self.c)
        
    def nature(self):
        self.dis = (self.b ** 2) - (4 * self.a * self.c)
        
        if self.dis > 0:
            sqrt_num = math.sqrt(self.dis)
            if sqrt_num.is_integer():
                print('Roots are Real, Distict & Rational.')
            else:
                print('Roots are Real, Distict & Irrational.')
        elif self.dis == 0:
            print('Roots are Real & Equal.')
        
        elif self.dis < 0:
            print('Roots are Complex & Distinct.')
            
    @classmethod
    def fromString(cls, abc):
        a,b,c = abc.split(',')
        return cls(int(a), int(b), int(c))

num = int(input("Number of times to run code: "))
while(num):
    val = input("Value 3 values(Format: a,b,c):")
    q = Quadratic.fromString(val)
    q.display()
    q.nature()
    num -= 1