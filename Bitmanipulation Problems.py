# Unique Numbers I

arr = [1,3,5,4,3,1,5]
xor = 0

for i in arr:
    xor ^= i
print(xor)

# Unique Numbers II

arr = [1,3,5,4,3,1,5,7]
xor = 0

for i in arr:
    xor ^= i

n = xor
pos = 0

while n:
    if n&1:
        break
    pos += 1

a = []

for i in arr:
    if i&(1<<pos):
        a.append(i)
    
e1 = 0
e2 = 0

for i in a:
    e1 ^= i
e2 = xor ^ e1

print(e1, e2)

# Unique Numbers III

arr = [1,3,5,4,3,1,5,5,3,1]
sum_arr = [0] * 32

for x in arr:
    i = 0
    while x:
        sum_arr[i] += (x&1)
        i += 1
        x = x>>1
        
sum_arr = list(map(lambda x: x % 3, sum_arr))

result = 0

for i in range(32):
    result += sum_arr[i]*(2**i)
    
print(result)

# Subsets

s = 'abcdef'
n = len(s)

for x in range(1<<n):
    sub = ""
    i = 0
    while x:
        if x&1:
            sub += s[i]
        i += 1
        x = x>>1
    print(sub)