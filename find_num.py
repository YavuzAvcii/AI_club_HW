import random

lower_bound = 1
upper_bound = 100
rand_num = random.randint(lower_bound, upper_bound)
guess = None

while(rand_num != guess):
    guess = int(input(f"Try to guess the number! between {lower_bound} and {upper_bound} \n"))
    if guess < lower_bound or guess >  upper_bound:
        print("The number you entered is out of range")
    elif (guess > rand_num):
        print("it is less than your guess")
        upper_bound = guess
    elif (guess < rand_num):
        print("it is greater than your guess")
        lower_bound = guess

print("Congrats you found the number!!")
