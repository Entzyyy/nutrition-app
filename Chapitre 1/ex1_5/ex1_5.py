file_name = input("enter file name (without extension): ")
file_path = f"Chapitre 1\\ex1_5\\{file_name}.txt"


file = open(file_path, "r", encoding="utf-8")

n_lines = 0
n_words = 0

for line in file: 
    n_lines += 1
    n_words += len(line.split())
    print(line.split())

file.close()
output_string = f"this file contains {n_lines} lines and {n_words} words."
print(output_string)

