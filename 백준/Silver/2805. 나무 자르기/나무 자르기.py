N, goal = map(int,input().split())
seq = list(map(int, input().split()))

def possible(cut):
    return sum([ max(s-cut, 0) for s in seq]) >= goal
l, r = 0, 10**9
while l < r:
    mid = (l + r +1) // 2
    if possible(mid):
        l = mid
    else:
        r = mid-1
print(l)