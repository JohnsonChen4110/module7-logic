# This script contains a program for a simple guessing game!

# Define a function `print_hot_or_cold()` that takes in two arguments (the `target`
# and the `guess`), and prints out an appropriate message based on how close
# the guess is to the target:
#
# Distance    Message
# -------------------
# The same    "got it!"
# Within 1	  "scalding hot"
# Within 3	  "very warm"
# Within 5	  "warm"
# Within 8	  "cold"
# Within 13	  "very cold"
# > 13 away	  "icy freezing miserably cold"
#
# Be sure to consider both positive AND negative distances!
# BONUS: Also print out whether the guess is high or low
import random

def high_or_low(target, guess):
    if target > guess:
        print("the guess is low")
    if target < guess:
        print("the guess is high")

def print_hot_or_cold(target, guess):
    if target == guess:
        print("got it!")
    elif abs(guess - target) <= 1:
        print("scalding hot")
        high_or_low(target, guess)
    elif abs(guess - target) <= 3:
        print("very warm")
        high_or_low(target, guess)
    elif abs(guess - target) <= 5:
        print("warm")
        high_or_low(target, guess)
    elif abs(guess - target) <= 8:
        print("cold")
        high_or_low(target, guess)
    elif abs(guess - target) <= 13:
        print("very cold")
        high_or_low(target, guess)
    else:
        print("icy freezing miserably cold")
        high_or_low(target, guess)



# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is (use your previous function!). Note that
# you will need to convert the input into a number.
#
# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next module)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. This is an example of **recursion**.
def guess_number(target):
    print("Welcome to Guess_Number! Guess a number between 1-100. If you want to quit, enter 'quit' anytime")
    guess = input("Please enter a number to make a guess --> ")
    if guess == "quit":
        print("Goodbye~")
        return 
    guess = float(guess)
    count = 1
    while guess != target:
        print_hot_or_cold(target,guess)
        guess = input("Please make another guess --> ")
        if guess == "quit":
            print("Goodbye~")
            return
        guess = float(guess) 
        count += 1
    print("Congrats! You got it using %d trials!" %count)
    


# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# use of the range of numbers before asking them for a guess.


if __name__ == '__main__':
    guess_number(random.randint(1,100))
