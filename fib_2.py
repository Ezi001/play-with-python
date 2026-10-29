l = 1
m = 2

sum = 2
n = 0

while n < 4000000:
    n = l + m
    if n % 2 == 0:
        sum += n

    l = m
    m = n

print(sum)