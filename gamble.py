#!/usr/bin/env python3

from random import getrandbits

balance = int(input("How many INR do you have? "))

while balance > 0:
    amount = int(input("Gamble how many INR: "))
    flip = getrandbits(1)
    if flip:
        print("Fail :(")
    else:
        print("Success! ")
    balance += (1-2*flip) * amount
    print("Balance: "+str(balance))

