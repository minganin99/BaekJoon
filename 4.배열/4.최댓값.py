n_list = []
for i in range(9):
    n_list.append(int(input()))
max = max(n_list)
min = min(n_list)

print(max)
print(n_list.index(max)+1)