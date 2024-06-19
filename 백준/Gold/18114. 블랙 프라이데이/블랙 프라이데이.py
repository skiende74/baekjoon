from bisect import bisect
N, goal = map(int,input().split())
seq = list(map(int,input().split()))
seq.sort()
seq_set = set(seq)
def solve():
    if goal in seq_set: return True
    i,j = 0, N-1
    while i<j:
        s1, s3 = seq[i], seq[j]
        if s1+s3 == goal: return True
        elif s1+s3 > goal: j -= 1
        else:
            if goal-s1-s3 in seq_set and s1<goal-s1-s3<s3: return True
            i += 1
    return False
print(1 if solve() else 0)