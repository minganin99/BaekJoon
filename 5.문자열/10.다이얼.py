num_str = input()
num_lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
tot = 0
for alph in num_str:
    for i in num_lst:
        if alph in i:
            num = int(num_lst.index(i)) + 3
            tot += num
print(tot)            