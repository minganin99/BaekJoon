num1, num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2:
    res = num1
else:
    res = num2
print(res)
