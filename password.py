import random
import string

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

letters = random_char(10)

password = letters + str(random.randint(10000, 1000000))

print("Password: " + password)