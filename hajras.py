import random
import string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + "!@#$%^&*()"
password = ''.join(random.choice(characters) for _ in range(length))
print("Your strong password is:", password)