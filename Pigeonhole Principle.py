# Divisible Subset

arr = [4,6,9]
n = len(arr)

for i in range(1,n):
    arr[i] += arr[i-1]
    
for i in range(n):
    arr[i] %= n

count = 0
for i in range(n):
    if arr[i] == 0:
        count += 1
    else:
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                count += 1
print(count)

# Gray Code Similar

arr = [1,0,2,3,7]
n = len(arr)
  
flag = False    
    
if n >= 130:
    flag = True
else:
    for i in range(n):
        s = set()
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]^arr[j]^arr[k]^arr[l] == 0:
                        flag = True
if flag:
    print("Yes")
else:
    print("No")