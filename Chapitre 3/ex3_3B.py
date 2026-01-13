from random import choice
from string import ascii_lowercase # lettres minuscule

def search_word_it(l,s):
    for i in range(0, len(l)):
        if l[i] == s:
            return i
        # else:
        #     print("Still searching")
    return -1

def search_word_rec(l,s,actual_position=0): # default value for actual_position is 0 when no other value given
    if actual_position == len(l): # non trouvé
        return -1
    elif l[actual_position] == s: # trouvé
        return actual_position
    else:
        actual_position += 1
        return search_word_rec(l,s,actual_position) # appel de la fonction avec nouvelle position

def search_dicho_it(l,s):
    actual_position = len(l)//2 # le milieu de la liste
    found = False

    while not found:
        if l[actual_position] == s:
            found = True
        elif l[actual_position] < s: # on continue à chercher dans la partie supérieure
            actual_position = (actual_position + actual_position*2) // 2
        elif l[actual_position] > s:
            actual_position //= 2
        elif actual_position == 0 or actual_position == len(l):
            return -1
    return actual_position

list_of_words = []

for i in range(998):
    # générer un mot (sans sens) d'une longueur de 3 caractères)
    # (séléctionnés parmi les lettres minuscules ascii_lowercase)
    temp_word = choice(ascii_lowercase) + choice(ascii_lowercase)+choice(ascii_lowercase)
    list_of_words.append(temp_word)

print(list_of_words)

# position_of_word = search_word_it(list_of_words, "abc") iterativ
position_of_word = search_word_rec(list_of_words, "abc")

if position_of_word != -1:
    print(f"First occurence of {list_of_words[position_of_word]} at position: {position_of_word}")
else:
    print("word not found")

# pour la recherche dichotomique, on trie la liste (utiliser: .sort())

list_of_words.sort() # pas nécessaire d'écrire list_of_words = list_of_words.sort()
print(list_of_words)
print(search_dicho_it(list_of_words,"abc"))