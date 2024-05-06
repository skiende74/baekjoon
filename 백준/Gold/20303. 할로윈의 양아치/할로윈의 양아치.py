import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
seq = [0]+list(map(int,input().split()))
parent = [i for i in range(N+1)]

def union(i,j):
    r1,r2 = find(i), find(j)
    parent[max(r1,r2)] = min(r1,r2)

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

for _ in range(M):
    i, j = map(int,input().split())
    union(i,j)

counts = [1]*(N+1)
for i in range(1,N+1):
    if i!= parent[i]:
        r = find(i)
        seq[r] += seq[i]
        counts[r] += counts[i]

dp = [0]*(K+1)
for i in range(1, N+1):  
    if i != parent[i]: continue  
    for j in range(K-1, counts[i]-1, -1):  
        dp[j] = max(dp[j], dp[j-counts[i]] + seq[i]) 

print(max(dp))