a = 0
while a == 0:
    number= input("Plese enter a number: ")
    try:
       val = int(number)
       print(int(number) * int(number))
    except ValueError:
       print("WRONG")
