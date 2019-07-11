#Jake Nenadic
#Findnding the index number of a gven word


WORDS = ["LIVE","SIMPLY","THAT","OTHERS","MIGHT","SIMPLY"]

guess =input("Words might include SIMPLY, OTHERS and LIVE. Please enter a word: ")

for i, j in enumerate(WORDS):
    if j == guess:
        print(i)
else:
    if j==guess== False:
        print("sorry. Your word is wrong")
  
