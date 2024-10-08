ches_lst = [1,1,2,2,2,8]
n_lst = list(input().split())
for i in range(6):
    if ches_lst[i] - int(n_lst[i]) == 0:
        n_lst[i] = 0 
    elif ches_lst[i] - int(n_lst[i]) > 0:
        n_lst[i] = ches_lst[i] - int(n_lst[i])
    else:
        n_lst[i] = ches_lst[i] - int(n_lst[i])
for i in n_lst:
    print(i, end=" ")