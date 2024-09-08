N, P = map(int, input().split())
seq = input()
conds = list(map(int, input().split()))
counts = {"A":0,"G":0,"C":0,"T":0}
for i in range(P): counts[seq[i]] += 1

ans = 0
if counts["A"] >= conds[0] and counts["C"]>= conds[1] \
and counts["G"]>= conds[2] and counts["T"] >= conds[3]:
    ans += 1
for i in range(P,N):
    counts[seq[i]] += 1
    counts[seq[i-P]] -= 1
    if counts["A"] >= conds[0] and counts["C"]>= conds[1] \
        and counts["G"]>= conds[2] and counts["T"] >= conds[3]:
        ans += 1
print(ans)