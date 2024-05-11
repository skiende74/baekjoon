N = int(input())
seq = list(map(int,input().split()))
seq.sort()

min_val = 3*10**9 +1

for i in range(N-2):
    l = i+1
    r = N-1
    while l<r:
        val = seq[i]+ seq[l] + seq[r]
        if abs(val) < min_val:
            min_val = abs(val)
            ans = (seq[i], seq[l], seq[r])
        if val < 0:
            l+=1
        elif val > 0:
            r-=1
        else: break
print(*ans)