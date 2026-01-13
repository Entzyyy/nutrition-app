file_name = f"Challenges\\aline-codes.txt"

file = open(file_name, "r")

aline_codes = {}

for line in file:
    # read_names = line.strip("\n") # still a string
    # read_names = read_names.split(" ") # now a list

    # names_dict[read_names[0]] = read_names[1], read_names[2], read_names[3], read_names[4]
    short = line[0:3]
    name = line[4:]
    aline_codes[short] = name

print(aline_codes)
file.close()

file_path = f"Challenges\\aline-prices.txt"
file = open(file_name, "r")

aline_prices = {}
for line in file:
    line_list = line.split()
    short = line_list[0]
    price = float(line_list[1])
    aline_prices[short] = price

file.close()


