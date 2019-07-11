#Word jumble
#Jake Nenadic
#working

import random

# creates a sequence of words to pick from
WORDS = ("python", "jumble", "easy", "answer", "xylophne")
#pick one word randomly from the sequence 
word = random.choice(WORDS)
#creat a variable to use later on
correct = word

jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word [:position] + word[(position + 1):]
#game starts
print(
"""
                       Welcom to the word jumble!
        unscrable the letters to make a word.
"""
)
print(" the jumble is", jumble)
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("sorry that is not right, try again")
    guess = input("your guess: ")
if guess == correct:
    print("correct!")
print("Thanks for playing.")
