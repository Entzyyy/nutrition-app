from functions_2B.my_math_functions import fact
from functions_2B.my_string_functions import how_many_different_vowels
from functions_2B.my_other_functions import count_digits

text = input("Entrez votre texte: ")

print(f"Votre texte contient {how_many_different_vowels(text)} voyelles différentes et {count_digits(text)} chiffres")
print(f"Calculons les factorielles: !{how_many_different_vowels(text)} = {fact(how_many_different_vowels(text))} et !{count_digits(text)} = {fact(count_digits(text))}")
