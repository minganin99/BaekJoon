N, M = map(int, input().split())
n_list = []
i = 0
while i < N:
    n_list.append(i+1)
    i+=1
    
for i in range(M):
    i, j = map(int, input().split())
    temp = n_list[i-1]
    n_list[i-1] = n_list[j-1]
    n_list[j-1] = temp

for i in n_list:
    print(i, end = " ")