
N, goal = map(int,input().split())
seq = list(map(int,input().split()))

def possible(cut):
    return sum([ max(0, s-cut) for s in seq]) >= goal

l, r = 0, 10**9
while l < r:
    mid = (l + r) // 2

    if possible(mid):
        l = mid+1
    else: 
        r = mid

print(l-1)