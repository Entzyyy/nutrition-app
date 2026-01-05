from functions_2B.ex1_0 import fact
from functions_2B.my_string_functions import string_is_empty

n = int(input("Enter an integer: "))
m = fact(n)
print(f"{n}! = {m}")

text = "hello world!"
print(string_is_empty(text))

def add_one_sec(h, m, s):
    if 0<=24 and 0<=m<60 and 0<=s<60:
        s += 1
        if s==60:
            s = 0
            m += 1
            if m==60:
                m = 0
                h += 1
                if h==24:
                    h = 0
        output_string = f"<< {h:02} {m:02} {s:02} >>"
        return output_string
    else:
        return "Arguments invalides"
    

def no_vowels(s):
    vowels = "aeiouAEIOU"
    for character in s:
        if character in vowels:
            return False
    return True

def count_digits(s):
    digits = "0123456789"
    counter = 0
    for character in digits:
        if counter in digits:
            counter += 1
    return counter

def how_many_vowels(s):
    vowels = "aeiouAEIOU"
    number_of_vowels = 0
    for character in s:
        if character in vowels:
            number_of_vowels += 1
    return number_of_vowels

def how_many_different_vowels(s):
    s = s.lower()
    vowels = "aeiouAEIOU"
    vowels_found = ""
    for character in s:
        if character in vowels:
            if not(character in vowels_found):
                vowels_found = vowels_found + character
    return len(vowels_found)