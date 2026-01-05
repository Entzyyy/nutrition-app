from random import randint

print("Hello Again!")

for i in range(100):
    print(i)

for i in range(100):
    print(i+1)

for i in range(10):
    print(i, end=(i-1)*f"{i}")

print()
for i in range(10):
    if i < 9:
        print(i, end=",")
    else:
        print(i)

random_number = randint(0,20)
user_number = int(input("Enter number from 0 to 10: "))

while random_number != user_number:

    if random_number > user_number:
        user_number = int(input("Enter a bigger number: "))
    elif random_number < user_number:
        user_number = int(input("Enter a smaller number: "))

print("correct")