N = int(input())
seq = [int(input()) for _ in range(N)]
seq.sort()
seq_set = set(seq)

max_cnt, cnt = 1, 1

for i in range(N):
    cnt = len([ j for j in range(seq[i], seq[i]+5)
        if j in seq_set])
    max_cnt = max(max_cnt, cnt)
print(5-max_cnt)
