from math import ceil
N, L = map(int,input().split())
ponds = [list(map(int,input().split())) for _ in range(N)]
ponds.sort()

last = 0
cnt, ans = 0, 0
for s, e in ponds:
    s = max(s, last)
    cnt = ceil((e-s)/L)
    ans += cnt
    # print(s,e,ceil((e-s)/L))
    last =  s+cnt*L
print(ans)