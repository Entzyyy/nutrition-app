file_name = "Chapitre 1\\ex0\\names.txt"

file = open(file_name, "r")
names_dict = {}

for line in file:
    read_names = line.strip("\n") # still a string
    read_names = read_names.split(",") # now a list
    # read_names = ["Anne", "35"]
    # names_dict = {read_names[0]}
    # shoes_dict = {read_names[1]}
    names_dict[read_names[0]] = read_names[1]

print(names_dict)

# my_dict = {}
# my_dict ["LAML"] = "LAMl"