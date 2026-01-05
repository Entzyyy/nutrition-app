def pgcd(a, b):
    return b if a % b == 0 else pgcd(b, a % b)


class Fraction: # immer majuscule
    def __init__(self, new_n=0, new_d=1): # constructor
        self.n = new_n
        self.d = new_d # if new_d != 0 else 1
        # self.simplify()

    def set_d(self, new_d):
        self.d = new_d if new_d != 0 else 1
        self.simplify()

    def simplify(self):
        if self.d < 0:
            self.n, self.d = -self.n, -self.d
        p = pgcd(abs(self.n), self.d)
        self.n //= p
        self.d //= p

    def invert(self):
        if self.n != 0:
            self.n, self.d = self.d, self.n
        else:
            print("Erreur : inverse de 0 !")

    def add(self, other):
        self.n = self.n * other.d + other.n * self.d
        self.d *= other.d
        self.simplify()

    def subtract(self, other):
        self.n = self.n * other.d - other.n * self.d
        self.d *= other.d
        self.simplify()

    def multiply_by(self, other):
        self.n *= other.n
        self.d *= other.d
        self.simplify()

    def divide_by(self, other):
        if other.n != 0:
            self.n *= other.d
            self.d *= other.n
            self.simplify()
        else:
            print("Erreur : division par 0 !")

    def __str__(self):
        return f"{self.n}/{self.d} ({self.n/self.d})"

    # a) is_zero() - teste si la fraction vaut 0 (return type: boolean - True ou False) 
    def is_zero(self):
        if self.n == 0:
            return True
        return False
    
    # b) is_integer() - teste si la fraction est un entier (si d divise n) (return type boolean)
    def is_integer(self):
        if self.n % self.d == 0:
            return True
        return False
    
    # c) is_equal_to(other) - teste si la fraction est égale à une autre fraction donnée en paramètre (return type boolean)
    def is_equal_to(self, other):
        self.simplify()
        other.simplify()
        if self.n == other.n and self.d == other.d:
            return True
        return False
    
    # d) opposite() - change le signe de la fraction  (pas de return - les valeurs elles-mêmes changent - SELF)
    def opposite(self):
        self.n = -self.n
    
    # e) power(k:int) - élève la fraction à la puissance k (k est entier) 
    def power(self,k):
        self.simplify()
        self.n = self.n**k
        self.d = self.d**k
    



# 1/3 + 4/5 - 42/70 * 5/20

f1 = Fraction(1,3)
f2 = Fraction(4,5)
f3 = Fraction(-42,70)
f4 = Fraction(5,20)

f3.multiply_by(f4)
f3.add(f1)
f3.add(f2)

print(f3)

# test des nouvelles méthodes
f5 = Fraction(0,4)
print(f5.is_zero())

f6 = Fraction(42,7)
print(f6.is_integer())

f7 = Fraction(6,10)
f8 = Fraction(3,5)
print(f7.is_equal_to(f8))
print(f8.is_equal_to(f1))

f9 = Fraction(2,5)
f9.opposite()
print(f9)

f10 = Fraction(2,3)
f10.power(3)
print(f10)

