from bisect import bisect
N, goal = map(int,input().split())
seq = [0]+list(map(int,input().split()))
seq.sort()
ans = 0
def solve():
    if goal in seq: return True
    for i, s in enumerate(seq):
        for j in range(i+1, N+1):
            s2 = seq[j]
            a = bisect(seq, goal-s-s2, j+1) -1
            if j+1<=a<=N and seq[a] == goal-s-s2: return True
    return False
print(1 if solve() else 0)