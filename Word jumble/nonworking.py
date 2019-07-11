#Word jumble
#Jake Nenadic
#nonworking
score = 0
import random

# creates a sequence of words to pick from
WORDS = ["abcdefghijklmnopqrstuvwxyz"]
#pick one word randomly from the sequence 
word = random.choice(WORDS)
#creat a variable to use later on
correct = word

jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[(position):]
    word = word [:position] + word[(position + 1):]
    # it should be  position = random.randrange(len(word))
    #jumble += word[position]
    #word = word [:position] + word[(position + 1):]
#game starts
print(
"""
                       Welcom to the word jumble!
        unscramble the letters to make a word.
"""
)
print(" the jumble is", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("sorry that is not right, try again")
    guess = input("your guess: ")
if guess == correct:
    print("correct!")
    score = score+1
    print("You got", score,"point")
print("Thanks for playing.")
input("press enter to exit")
