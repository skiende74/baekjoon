import sys
input = sys.stdin.readline

N, S = map(int,input().split())
seq = list(map(int,input().split()))

INF = 10**9
ans = INF
j=0
total = seq[0]
for i in range(N):
    while j<N and total<S: 
        j += 1
        if j!=N: total += seq[j]
    if j==N: break
    ans = min(ans, j-i+1)
    total -= seq[i]
print(ans if ans != INF else 0)