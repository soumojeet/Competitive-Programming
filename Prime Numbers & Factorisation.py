# Primes Till N

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
n = 100

for i in range(2,n+1):
    if isPrime(i):
        print(i, end=" ")

# Prime Sieve

n = 100
sieve = [1]*(n+1)

sieve[0] = sieve[1] = 0

for i in range(2,n+1):
    if sieve[i] == 1:
        print(i, end=" ")
        for j in range(i*i,n+1,i):
            sieve[j] = 0

# Prime Queries

n = 25
sieve = [1]*(n+1)

sieve[0] = sieve[1] = 0

for i in range(2,n+1):
    if sieve[i] == 1:
        for j in range(i*i,n+1,i):
            sieve[j] = 0

for i in range(1,n+1):
    sieve[i] += sieve[i-1]
    
a, b = 2, 11

print(sieve[b] - sieve[a-1])

# Prime Factorisation

#O(N)
print("N Solution")
n = 223092870
i = 2
while i <= n:
    if n%i == 0:
        count = 0
        while n%i == 0:
            count += 1
            n = n//i
        print(f'{i}^{count}',end=" ")
    i += 1

#O(SQRT(N))
print("\nSQRT(N) Solution")
n = 223092870
i = 2
while i*i <= n:
    if n%i == 0:
        count = 0
        while n%i == 0:
            count += 1
            n = n//i
        print(f'{i}^{count}',end=" ")
    i += 1
if n!= 1:
    print(f'{n}^1')

# Prime Factorisation Using Sieve

n = 100
sieve = [1]*(n+1)

sieve[0], sieve[1] = 0, 1

for i in range(2,n+1):
    if sieve[i] == 1:
        for j in range(i,n+1,i):
            if sieve[j] == 1:
                sieve[j] = i
factors = []
n = 72
while n != 1:
    factors.append(sieve[n])
    n = n//sieve[n]
    
print(*factors)