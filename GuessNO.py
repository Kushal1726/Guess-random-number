import random
import math

lower = int(input("Enter Lower bound : "))
upper = int(input("Enter Upper bound : "))

x = random.randint(lower, upper)
print("\n \t You've only",
       round(math.log(upper - lower + 1, 2)),
                "chances to Guess intger! \n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess=int(input("Guess a number:-"))
if x == guess:
    print("congratulations you did it in", 
          count, " try")
    ("break")

elif x > guess:
    print("You guessed to small!")
elif x < guess:
    print("You guessed to high!")

if count >= math.log(upper - lower + 1, 2):
    print("\n the number is %d " % x)
    print("\t Better Lack Next time !")





