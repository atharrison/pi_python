import random
import string


for y in range(0, 8):
    letters = [" "," "," "," "," "," ",]
    for y in range (0, 6):
        letters[y] = random.choice(string.ascii_letters).upper()
    print(" ".join(letters))