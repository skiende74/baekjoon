import sys
from bisect import bisect_left

sys.setrecursionlimit(2*10**5)

input = sys.stdin.readline
N, K = map(int,input().split())
jewels = [list(map(int,input().split())) for _ in range(N)]
jewels.sort(key=lambda x: -x[1])

parent = [i for i in range(K+1)]
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]
def union(i,j):
    r1,r2 = find(i), find(j)
    parent[min(r1,r2)] = max(r1,r2)

bags = [ int(input()) for _ in range(K)]
bags.sort()

ans = 0
for w, v in jewels:
    i = bisect_left(bags, w)
    i = find(i)

    if i != K:
        union(i,i+1)
        ans += v
print(ans)
