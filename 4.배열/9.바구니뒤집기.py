N, M = map(int, input().split())
n_list = [i for i in range(1, N+1)]

for n in range(M):
    i, j = map(int, input().split())
    tmp_list = n_list[i-1:j]
    tmp_list.reverse()
    n_list[i-1:j] = tmp_list
for i in n_list:
    print(i, end=" ")
