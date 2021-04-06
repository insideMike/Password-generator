import random
import string

password = []
characters_left = -1
pass_minimum_characters = int(input("What is the minimum password length:"))


def update_characters(number_of_characters):
    # Checking the number of characters remaining
    global characters_left
    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Number of characters out of range", characters_left)
    else:
        characters_left -= number_of_characters
        print("Left: ", characters_left)


pass_length = int(input("Enter the password length:"))

while pass_length < pass_minimum_characters:
    print("password is too short")
    pass_length = int(input("Enter the password length:"))
else:
    characters_left = pass_length

lowercase_letters = int(input("How many lowercase letters?"))
update_characters(lowercase_letters)

uppercase_letters = int(input("How many uppercase letters?"))
update_characters(uppercase_letters)

special_characters = int(input("How many special signs?"))
update_characters(special_characters)

digits = int(input("How many digits?"))
update_characters(digits)

if characters_left > 0:
    print("Missing characters will be completed with lowercase letters")
    lowercase_letters += characters_left
print()
print("Password length:", pass_length)
print("Lowercase:", lowercase_letters)
print("Uppercase:", uppercase_letters)
print("Special characters:", special_characters)
print("Digits:", digits)

for _ in range(pass_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    elif uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    elif special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1
    elif digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Generated password is:", "".join(password))
