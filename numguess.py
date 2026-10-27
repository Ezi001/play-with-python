import random

val = random.randint(0, 100)

print("Enter a number between 0 and 100.")
lam = 1

while lam == 1:
    val_usr = int(input())
    if val_usr < 0 or val_usr > 100:
        print("Choose valid value")
    if val_usr == val:
        print("You guessed correctly and win!")
        lam = 0
    elif val_usr < val:
        print("your too low!")
    else:
        print("You're too high!")
