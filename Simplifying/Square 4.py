a = 0
while a == 0:
    number= input("Plese enter a number: ")
    try:
       val = int(number)
       print(int(number) * int(number))
       exit = input("would you like to exit?")
       if exit == ("yes"):
            a = a + 1
       else:
            a = a + a
    except ValueError:
       print("WRONG")
       exit = input("would you like to exit?")
       
