# Ishak Boukellal and his friend Copilot
# Part 1: Create dictionary from aline-codes.txt
file_name = "Challenges\\aline-codes.txt"
file = open(file_name, "r")

aline_codes = {}
for line in file:
    short = line[0:3]
    name = line[4:].strip()
    aline_codes[short] = name

file.close()

# Part 2: Create dictionary from aline-prices.txt
file_name = "Challenges\\aline-prices.txt"
file = open(file_name, "r")

aline_prices = {}
for line in file:
    line_list = line.split()
    short = line_list[0]
    price = float(line_list[1])
    aline_prices[short] = price

file.close()

# Part 3: Create dictionary for each client from aline-orders.txt
file_name = "Challenges\\aline-orders.txt"
file = open(file_name, "r")

clients = {}
client_number = 1

for line in file:
    parts = line.strip().split()
    first_name = parts[0]
    last_name = parts[1]
    orders = parts[2:]
    clients[f"client{client_number}"] = [first_name, last_name] + orders
    client_number += 1

file.close()

# Part 4: Print order summary for each client
for client in clients:
    data = clients[client]
    first_name = data[0]
    last_name = data[1]
    items = data[2:]

    print(f"\nClient: {first_name} {last_name}")
    print("Commande:")
    total = 0
    for item in items:
        name = aline_codes[item]
        price = aline_prices[item]
        print(f"- {name}: €{price:.2f}")
        total += price
    print(f"Total à payer: €{total:.2f}")