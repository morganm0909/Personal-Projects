from datetime import date
import getpass

today = date.today()
d = today.strftime("%d/%m/%Y")

user_inp = input("Begin typing: ")

password = getpass.getpass("Enter a password to secure your entry: ")

file = "encrypted_file.txt"
with open(file, "w") as w2:
    encrypted = "".join([chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(user_inp)])
    w2.write(d + "\n")
    w2.write(encrypted)


    view = input("Would you like to view your entry? Type yes or no.")
    y = "Yes"
    n = "No"
    if view.lower() == y.lower():
        decrypt = "".split([chr(ord(c) ^ ord(password[i % len(password)])) for i, c in enumerate(user_inp)])
    else:
        print("Diary locked")

