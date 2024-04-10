N, C = map(int, input().split())
seq = [int(input()) for _ in range(N)]

seq.sort()

# 최인접거리 -> 공유기수
def func(dist):
    old = seq[0]
    c = 1
    for s in seq:
        if s-old<dist: continue
        old = s
        c += 1
    return c
def custom_bound(goal):
    left, right = 1, seq[-1]-seq[0]
    max_idx = 1

    while left<= right:
        mid = (left+right)//2

        if func(mid) >= goal:
            left = mid + 1
            max_idx = max(max_idx, mid)
        else: right = mid - 1

    return max_idx

print(custom_bound(C))