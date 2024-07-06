from collections import defaultdict
K = int(input())
seq = list(input())
N = len(seq)

counter = defaultdict(lambda: 0)
max_cnt = 1
j = 1
alpha = set([seq[0]])
counter[seq[0]] = 1
for i in range(N):
    while j<=i or j<N and (len(alpha)<K or seq[j] in alpha):
        alpha.add(seq[j])
        counter[seq[j]] += 1
        j += 1
    max_cnt = max(max_cnt, j-i)
    counter[seq[i]] -= 1
    if counter[seq[i]] == 0: alpha.remove(seq[i])

print(max_cnt)