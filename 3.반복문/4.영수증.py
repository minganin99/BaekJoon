X = int(input())
N = int(input())
i = 1
tot = 0
while i <= N:
    a, b = map(int, input().split()) 
    tot += a * b
    i += 1

if X == tot:
    print("Yes")
else:
    print("No")
    