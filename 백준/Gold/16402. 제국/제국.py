import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**4)
def union(i, j, num):
    u, v = find(i), find(j)
    if u == v: 
        if i != j:
            if num == 1: parent[i],parent[j] = i,i
            if num == 2: parent[i],parent[j] = j,j
        return
    if num == 1: parent[u],parent[v] = u,u
    if num == 2: parent[u],parent[v] = v,v

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

N, M = map(int,input().split())
kingdoms = [ input().split()[2] for _ in range(N)]
parent = { k:k for k in kingdoms }

for _ in range(M):
    kingdom1, kingdom2, num = input().split(',')
    k1, k2, num = kingdom1.split()[2], kingdom2.split()[2], int(num)
    union(k1,k2,num)

res = {find(k) for k in kingdoms}
print(len(res))
for r in sorted(res):
    print('Kingdom of', r)