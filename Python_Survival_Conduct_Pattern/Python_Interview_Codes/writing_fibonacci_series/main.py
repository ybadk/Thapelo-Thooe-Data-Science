fib = [0, 1]

# Range starts from 0 by default

n = 5

for i in range(n):
    fib.append(fib[-1] + fib[-2])


#Converting the list of intergers to string
print(','.join(str(e) for e in fib))

