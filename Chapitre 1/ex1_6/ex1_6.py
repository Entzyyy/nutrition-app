file_name = f"Chapitre 1\\ex1_6\\cours_bourse.txt"

file = open(file_name, "r", encoding="utf-8")

liste_cours = [] # liste vides

for line in file:
    temp_list = line.split()
    liste_cours += temp_list

print(liste_cours)

count = 0

for i in range (len(liste_cours)-1):
    if int(liste_cours[i+1]) > int(liste_cours[i]):
        count +=1

print(count)
file.close()