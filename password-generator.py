# This program generate the password
import random,string

print("Welcome to password generator")
#we are going to create a pool of words for password generation
letters=''.join(random.choices(string.ascii_letters,k=15))
digits=''.join(random.choices(string.digits,k=9))
symbols="!@#*&"
password=""
password+=random.choice(letters)
password+=random.choice(digits)
password+=random.choice(symbols)
#we are going to combine all the pool of words
pool_words=letters+symbols+digits
#we are going to ask the user for the length of password
user_input=int(input("\nEnter the length of password: "))
#we are going to generate the password by randomly selecting characters from the pool of words
for i in range (user_input-3):
    comp_choice=random.choice(pool_words)
    password+=comp_choice
print("\nYour strong password is :",password)    
print("\nThank you for using password generator")
