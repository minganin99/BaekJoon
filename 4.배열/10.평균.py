subject = int(input())
score_lst = list(map(int, input().split()))
max_score = max(score_lst)
for i in range(len(score_lst)):
    score_lst[i] = (score_lst[i]/max_score)*100
print(sum(score_lst)/len(score_lst))
# max_score = max(score_lst)