from math import gcd

class Fraction:
    def __init__(self, new_n, new_d): # constructeur de la classe
        self.n = new_n
        self.d = new_d

    def __str__(self):             # output
        s = f"{self.n} / {self.d} ({self.n/self.d:.2f})" # chaine s qui sera renvoyée
        return s

    def set_d(self, new_d):
        self.d = new_d

    def simplify(self):
        pgcd = gcd(self.n, self.d)
        self.n = self.n // pgcd     # self.n // = pgcd
        self.d = self.d // pgcd
    
    def invert(self):
        self.n, self.d = self.d, self.n
    
    def add(self, other):
        result_d = self.d * other.d
        result_n = self.n * other.d + other.n * self.d

        self.n = result_n
        self.d = result_d

        self.simplify()
    
    def multiply_by(self, other):
        self.n = self.n * other.n
        self.d = self.d * other.d
        self.simplify()

    def divide_by(self, other):
        self.n = self.n * other.d
        self.d = self.d * other.n
        self.simplify()



# partie principale

f1 = Fraction(6,7)          # lorsqu'on crée une nouvelle instance en appellant
f2 = Fraction(47,101)       # le nom de la classe, le constructeur __init__() est appelé

print(f1)   # lorsqu'on utilise print avec une instance de la classe
print(f2)   # le nom de la classe, le constructeur __str__() est appelé

f1.set_d(8)
print(f1)

f3 = Fraction(48,64)
print(f3)
f3.simplify()
print(f3)
f3.invert()
print(f3)

f4 = Fraction(3,4)
f5 = Fraction(7,6)
print(f4)
print(f5)

f4.add(f5)
print(f4)