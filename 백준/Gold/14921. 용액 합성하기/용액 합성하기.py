N = int(input())
seq = list(map(int,input().split()))
seq.sort()

l, r = 0, N-1
ans = 3*10**8
while l < r:
    if abs(ans) > abs(seq[l] + seq[r]):
        ans = seq[l] + seq[r]
    if seq[l] + seq[r] < 0: l += 1
    elif seq[l] + seq[r] > 0: r -= 1
    else: break
print(ans)
        