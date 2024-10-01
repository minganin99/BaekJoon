N, M = map(int, input().split())
n_list = []
i = 0
while i < N:
    n_list.append(0)
    i+=1
for i in range(M):
    a, b, c = map(int, input().split())
    while a <= b:
        n_list[a-1] = c
        a += 1
for i in n_list:
    print("%d" % i, end=" ")