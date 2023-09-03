# Binary Exponentiation

a, b = 2, 10
result = 1
while b:
    if b&1:
        result *= a
    a = a*a
    b = b>>1
print(result)

# Modular Exponentiation

mod = int(1e9+7)
a, b = 2, 100
result = 1
while b:
    if b&1:
        result *= a
        result = result%mod
    a = a*a
    a = a%mod
    b = b>>1
print(result)

# Fast Multiplication

a, b = 2, 10
result = 0
while b:
    if b&1:
        result += a
    a = a+a
    b = b>>1
print(result)

# Modular Multiplication

a, b = 2, 100
result = 0
while b:
    if b&1:
        result += a
        result = result%mod
    a = a+a
    a = a%mod
    b = b>>1
print(result)

# Matrix Exponentiation

def identity():
    result = []
    for i in range(2):
        result.append([0]*2)
        result[i][i] = 1
    return result

def matmul(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        T = [[1,1],[1,0]]
        result = identity()
        n -= 2
        while n:
            if n&1:
                result = matmul(result,T)
            T = matmul(T,T)
            n = n>>1
        return result[0][0]+result[0][1]

fibonacci(10)