n_list = []
for i in range(10):
    n = (int(input())) % 42
    n_list.append(n)
print(len(set(n_list)))
