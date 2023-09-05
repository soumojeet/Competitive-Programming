# Total No Divisor Till N

n = 10000
primes = [2,3,5,7,11,13,17,19,23,29]
m = len(primes)
ans = 0 
for i in range(1,1<<m):
    val = 1
    for j in range(m):
        if i>>j&1:
            val*=primes[j]
    bits = 0
    while i:
        if i&1:
            bits+=1
        i = i>>1
    if bits&1:
        ans += (n//val)
    else:
        ans -= (n//val)
print(ans)