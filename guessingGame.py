import random
number = random.randint(1,9)
num = int(input("enter your guess (must be between 1 and 9): "))
chance = 0

while chance<5:
    if(num < number):
        print("Your guess was too low")
    if(num > number):
        print("Your guess was too high")
    if num == number:
        print("Congratulations you won!")
        chance = 6
    if chance<5:
        num = int(input("enter your guess again: "))
        chance +=1

if chance == 5:
    print("no more guesses")