#No vowls
#Jake Nenadic

message = input("Enter message: ")
new_message = "*"
VOWELS =  "a","e","i","o","u"

print ( )
for letter in message:
    if letter.lower() in VOWELS:
        new_message = "*"
        print("A new string has been made:",new_message)

print("\n your message with out vowles in:", new_message)
input("")
