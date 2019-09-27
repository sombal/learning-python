from datetime import datetime

startTime = datetime.now()
primes = []
for n in range(2, 10001):
    for x in range(2, n):
        if n % x == 0:
            # print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        # print(n, 'is prime')
        primes.append(n)

print("Biggest prime in range:", primes[-1])
endTime = datetime.now()
print("Total runtime: " + str(endTime - startTime))
