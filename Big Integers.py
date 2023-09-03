# Big Addition

num1 = "912345678901234912389012345678901237891239012901290121238901289012890"
num2 = "912345678901234912389012345678901237891239012901290121238901289012890"

i = len(num1)-1
j = len(num2)-1
carry = 0
result = ""

while i>=0 and j>=0:
    carry += int(num1[i]) + int(num2[j])
    i, j = i-1, j-1
    last_digit = carry%10
    carry = carry//10
    result = str(last_digit) + result

while i>=0:
    carry += int(num1[i]) 
    i = i-1
    last_digit = carry%10
    carry = carry//10
    result = str(last_digit) + result
while j>=0:
    carry += int(num2[j])
    j = j-1
    last_digit = carry%10
    carry = carry//10
    result = str(last_digit) + result
    
if carry:
    result = str(carry) + result

print(result)

# Array & Integer Multiplication

def multiplication(num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    
    i = len(num1)-1
    carry = 0
    result = ""

    while i>=0:
        carry += int(num1[i]) * int(num2)
        i = i-1
        last_digit = carry%10
        carry = carry//10
        result = str(last_digit) + result
    
    if carry:
        result = str(carry) + result

    return result

def factorial(num):
    if num==1:
        return '1'
    num1 = str(num)
    num2 = num-1
    
    return multiplication(factorial(num2), num1)

# Large Factorial

print(factorial(50))