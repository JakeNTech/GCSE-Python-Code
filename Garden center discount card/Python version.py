#Jake Nenadic
#gardencenter discount card
from decimal import Decimal

cost = float(input("what have you spent in the garden center? "))
card = input("Do you have a loyalty card? ")

if card == ("no"):
    if cost >= float(100):
           cost=Decimal(cost*0.95)
           rounded=round(cost,2)
           print("£",rounded)
           print("You have a 5% discount, happy days")
    else:
           print("sorry no discount")
           print("why not get a  discount card")
elif card == ("yes"):
    if cost >= float(100):
           cost=Decimal(cost*0.85)
           rounded=round(cost,2)
           print("£",rounded)
           print("You have a 15% discount, happy days")
           
    elif cost >= float(50):
        cost=Decimal(cost*0.9)
        rounded=round(cost,2)
        print("£",rounded)
        print("You have a 10% discount, happy days")
        
    else:
        print("No discount")
else:
    print("WRONG")


print("Why not visit the happy hill coffe shop just off the A1?")
print("Thank you for shopping at happy hill garden center,please come again")     
           
