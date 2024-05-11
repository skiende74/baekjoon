N = int(input())
seq = list(map(int,input().split()))

l, r = 0, N-1
min_val = 2*10**9 +1
while l<r:
    val =  seq[l] + seq[r]
    
    if abs(val) < min_val:
        min_val = abs(val)
        ans = (seq[l],seq[r])
    if val == 0: break
    if val > 0: r-=1
    else: l+=1
print(*ans)    