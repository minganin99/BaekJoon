N = int(input())
res = N//4
i = 1
while i <= res: 
    if i != res:
        print("long ", end='')
    else:
        print("long int")
    i += 1
    