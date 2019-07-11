array = ["Cyber","Security","is","a","cool","subject"]
print("""
__________
| WELCOME |
----------
To continue please select the method of search you wish to preform:
1- Binary
2- Liner
3- I don't want to preform a serch at all
""")
user_selection = input("Please make your selection from the values above: ")
if user_selection > 3:
    print("nice try there")
    print("Please only enter a valid number")
elif user_selection == 2:
    print(array)
    to_find = str(input("Enter the item that you wish to search: "))
    for i in range(0,len(array)):
        if array[i] == to_find:
            print("Item found in position ",i)
            exit()
        else:
            print("Not in position",i)
        
    
