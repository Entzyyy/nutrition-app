from random import randint

list_of_coordinates = []

for i in range(10):
    x_temp = randint(-10,10)
    y_temp = randint(-10,10)
    coord_temp =(x_temp, y_temp)
    list_of_coordinates.append(coord_temp)

print(list_of_coordinates[2])
print(list_of_coordinates[5][0])
print(list_of_coordinates[8][1])

#

dict_jo_nee = {}

dict_jo_nee["Jo"] = ["Ja", "Oui", "Yes"]
dict_jo_nee["Nee"] = ["Nein", "Non", "No"]

dict_input_to_index = {}
dict_input_to_index["de"] = 0
dict_input_to_index["fr"] = 1
dict_input_to_index["en"] = 2

language = input("Enter a language (de,fr,en): ")
if language not in dict_input_to_index:
# ou bien: if language != "de" and language != "fr" and language != "en":
# ou bien: if language not in ("de","fr", "en"):
    print("Language not available")
else:
    word = input("Enter word (Jo or Nee): ")
    if word == "Jo" or word == "Nee":
        index_of_word = dict_input_to_index[language]
        translation_of_word = dict_jo_nee[word][index_of_word]
        print(translation_of_word)
    else:
        print("Word not in dictionary.")