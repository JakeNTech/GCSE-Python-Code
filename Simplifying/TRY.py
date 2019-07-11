number= input("Number: ")
try:
   val = int(number)
   print(int(number) * int(number))
except ValueError:
   print("That's not an int!")
