N, K = map(int,input().split())
seq = list(map(int,input().split()))

def is_possible(T):
    prev, i = N, N-1
    for _ in range(K):
        while seq[i] != 1: i += 1
        if i == prev: return False
        prev = i
        i -= T
        if i <= 0: return True
    return False

l, r = 0, N-1
while l < r:
    mid = (l+r) // 2
    if is_possible(mid): r = mid
    else: l = mid+1

print(l)