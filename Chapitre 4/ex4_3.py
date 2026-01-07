class Number:

    def __init__(self, new_value):
        self.value = abs(new_value)

    def __str_(self):
        s = f"value is {self.value}"
        return s

    def set_value(self, new_value):
        self.value = abs(new_value)

    def factorial(self):
        if self.value == 0:
            return 1
        else:
            fact = 1
            for i in range(1, self.value + 1):
                fact *=i
            return fact

    def sum_of_divisors(self):
        sum_div = 0
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                sum_div +=i
        return sum_div
    
    def reverse(self):
        list_digits = []
        temp_number = self.value

        while temp_number >= 1:
            list_digits.append(temp_number % 10)
            temp_number //= 10
        
        new_number = 0

        return list_digits

    def is_square(self):
        pass

    def is_prime(self):
        pass

    def is_perfect(self):
        pass

    def is_palinderome(self):
        pass

    def is_amicable_to(self, other):
        pass

my_number = Number(6)
print(my_number)
print(my_number.factorial())
print(my_number.sum_of_divisors())
print(my_number.reverse())