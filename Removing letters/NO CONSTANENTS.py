#No vowls
#Jake Nenadic

message = input("Enter message: ")
new_message = " "
CONSTANENTS =  "bcdfhjklmpqrstvwxyz"

print ()
for letter in message:
    if letter.lower() not in CONSTANENTS:
        new_message += letter
        print("A new string has been made:",new_message)

print("\n your message with out constanents in:", new_message)
input("")
