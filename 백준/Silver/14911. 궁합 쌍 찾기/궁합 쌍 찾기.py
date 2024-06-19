from collections import Counter
seq = list(map(int,input().split()))
seq.sort()
seq_set = set(seq)

seq_cnt = Counter(seq)
goal = int(input())

answers = set()
for i, s in enumerate(seq):
    if goal-s in seq_set and s<=goal-s:
        if s==goal-s and seq_cnt[s] == 1: continue
        answers.add((s,goal-s))

answers = list(sorted(list(answers)))
for ans in answers:
    print(*ans)
print(len(answers))