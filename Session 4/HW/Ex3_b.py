from random import choice
import random
list = ["Rainbow", "Unicorn", "Cats", "Dogs"]

word = random.choice(list)
correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#game
print("Guess the word:")
print("The jumble is: ", jumble)

guess = input("Your guess:")

if guess != correct:
    print("Incorrect! Please try again")
    guess = input("Your guess:")

if guess == correct:
    print("You've made it! Congrats")
