#The import of an applications
import random
import string

#Telling python what characters he can use, using string application
digits = string.digits
letters = string.ascii_letters

#Putting all characters together
passwordCharacters = digits + letters

#Asking the user how much characters he wants his/hers password to be 
howMuchCharacters = int(input("How much characters do you want your password to have? »"))

#Putting together the password using the random application
password = [random.choice(passwordCharacters) for i in range(howMuchCharacters)]

#Printing the password without any spaces
print("".join(password))