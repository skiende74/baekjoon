from bisect import bisect_left
N = int(input())
seq = list(map(int,input().split()))

seq.sort()
min_ = 3*10**9
for i, s in enumerate(seq):
    y = bisect_left(seq, -s, i+1)
    for yy in range(y-1,y+1):
        if i == yy: continue
        if yy < N and abs(s+seq[yy]) < min_:
            ans = f'{s} {seq[yy]}'
            min_ = abs(s+seq[yy])
print(ans)