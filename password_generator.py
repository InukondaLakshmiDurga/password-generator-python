import random
import string

def generate_password(length):
    # Letters (a-z, A-Z), digits (0-9), and symbols (@#$%)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for length
length = int(input("length of password : "))
print("Generated Password: ", generate_password(length))