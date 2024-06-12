import sys
input = sys.stdin.readline
N= int(input())
seq = [tuple(map(int,input().split())) for _ in range(N)]
seq.sort()

res = 0
cur_s = seq[0][0]
cur_e = seq[0][1]
for s, e in seq[1:]:
    if s > cur_e:
        res += cur_e - cur_s
        cur_s = s
    cur_e = max(cur_e, e)
print(res+cur_e-cur_s)