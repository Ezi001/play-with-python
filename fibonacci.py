fib = [] # Fibonaccisekvensen

l = 1
m = 2

fib.append(l) # Vi må ha de første to tallen i sekvensen før løkken
fib.append(m)

n = 0  # n må være definert før løkken

while n < 4000000: # n er det seneste tallet i sekvensen
    n = l + m
    fib.append(n)

    l = m # l og m må oppdateres
    m = n


sum = 0 # Summen må være definert før løkken

for n in fib:
    if n % 2 == 0:
        sum += n

print(sum) # Sånn at vi får vite hva summen er


