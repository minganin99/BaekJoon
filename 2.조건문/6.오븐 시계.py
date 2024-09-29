A, B = map(int, input().split()) 
C = int(input()) 

h = C // 60
m = C % 60

H = A + h
M = B + m

if M >= 60:
    if H >= 23:
        H -= 23
        M -= 60
    else:
        H += 1
        M -= 60
else:
    if H >= 24:
        H -= 24

print(H, M)




