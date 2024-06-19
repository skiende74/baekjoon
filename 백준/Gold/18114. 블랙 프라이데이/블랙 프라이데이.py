from bisect import bisect
N, goal = map(int,input().split())
seq = [0]+list(map(int,input().split()))
seq.sort()
seq_set = set(seq)
ans = 0
def solve():
    if goal in seq_set: return True
    for i, s in enumerate(seq):
        for j in range(i+1, N+1):
            s2 = seq[j]
            if goal-s-s2 in seq_set and goal-s-s2 > s2: return True
    return False
print(1 if solve() else 0)