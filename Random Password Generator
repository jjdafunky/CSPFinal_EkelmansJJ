#prints random password at desired length and with the desired starting phrase

import random
import string

length=int(input("Length of password: "))
base= str(input("Starting phrase: "))
length = length-len(base)-1

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols

rando = random.sample(all,length)
password = "".join(rando)
print(base+password)
