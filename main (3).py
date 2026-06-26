# Password Generator Program

import random

print("\n--- PASSWORD GENERATOR ---")

n = int(input("Enter how many characters you want in password: "))

ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"

pwd = ""

for i in range(n):
    x = random.choice(ch)
    pwd = pwd + x

print("Your password is:", pwd)