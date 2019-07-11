import random
print("I am a magic computer that knows your current mood......")
print("I can feel your mood particals crossing my CD drive....")

mood = random.randint(1, 3)

if mood == 1:
    #Happy face
    print( \
    """
            -------------- 
            |            |
            |            |
            |    0    0  |
            |       <    |             
            |            |
            |   .     .  |
            |    . . .   |
            |            |
            |            |
            --------------
            you are happy """)
 
elif mood == 2: 
     #Okay
     print( \
    """
            -------------- 
            |            |
            |            |
            |    0    0  |
            |       <    |             
            |            |
            |   -------- |
            |            |
            |            |
            |            |
            -------------- """)
 
if mood == 3:
    print ( \
    """
            -------------- 
            |            |
            |            |
            |    0    0  |
            |       <    |             
            |            |
            |   . . . .  |
            |  .       . |
            |            |
            |            |
            -------------- """)



print("I may be wrong but nevermind i bet i was close though")
print("why not have a go at the word jumbler game")
input("ENTER TO EXIT")

