def is_multiple_of_5_or_6(x):
    return ((x % 5) == 0) or ((x % 6) == 0)

def nth_multiple_of_5_or_6(n):
    found = 0
    guess = -1
    while found <= n:
        guess += 1
        if is_multiple_of_5_or_6(guess):
            found += 1
    return guess

print("De første ti tallene som er delelig med 5 eller 6: ")
i = 0
while i < 10:
    print(nth_multiple_of_5_or_6(i), end=" ")
    i += 1
print()