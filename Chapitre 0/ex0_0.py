from random import randint

print("Hello Again!")

for i in range(100):    # honnertmol eppes man doweinst fànk heen bei null un a geet bis 99
    print(i)

for i in range(100):
    print(i+1)   

for i in range(10):
    print(i, end=(i-1)*f"{i}")

print()

for i in range(10):
    if i < 9:                 # if fir datt herno keen Komma an der leschter Rei ass
        print(i, end=",")
    else:
        print(i)

# randint(0,n) = [0,n]
# randrange(0,n) = [0,n[
#random() = [0,1] all dei dertescht 0,1 ; 0,2

random_number = randint(0,20)  # [0,20]

user_number = int(input("Enter a number between 0 and 20: "))

while random_number != user_number:
    if random_number > user_number:
        user_number = int(input("Enter a bigger number: "))
    elif random_number < user_number:                          # keint een och else huelen mee mat elif ass een sech mei secher
        user_number = int(input("Enter a smaller number: "))
    
print("correct")    # random_number == user_number