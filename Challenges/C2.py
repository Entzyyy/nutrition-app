file_name = "Challenges\\capitals.txt"
file = open(file_name, "r")

country_capital = {}

for line in file:
    country = line.strip("\n") # still a string
    country = country.split(",") # now a list
    country = (country[0])
    capital = (country[1])
    
    country_capital[country] = capital

file.close()


file_name = "Challenges\\population.txt"
file = open(file_name, "r")

population = {}

for line in file:
    pop = line.strip("\n") # still a string
    pop = pop.split(",") # now a list
    capital = (pop[0])
    pop = (pop[1])


    population[capital] = pop

file.close()



print(f"The capital of {country_capital[country]} is {country_capital[capital]} ({population[capital]})")