from bisect import bisect_left, bisect_right
N = int(input())
seq = list(map(int, input().split()))
seq.sort()

answer = 0
for i in range(N-1):
    for j in range(i+1, N-1):
        u1, u2 = seq[i], seq[j]
        if u1+u2+seq[j+1] > 0: continue
        u = bisect_right(seq, -u1-u2)
        l = max(j+1, bisect_left(seq,-u1-u2))
        answer += u-l
print(answer)