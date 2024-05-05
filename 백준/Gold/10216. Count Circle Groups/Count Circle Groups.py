import sys
input= sys.stdin.readline
T = int(input())
def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1] = min(r1,r2)
    parent[r2] = min(r1,r2)

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

def nearby(e1, e2):
    i,j,r = e1
    i2,j2,r2 = e2
    return (i-i2)**2+(j-j2)**2 <= (r+r2)**2

for _ in range(T):
    N = int(input())
    enemies = [list(map(int,input().split())) for _ in range(N)]
    parent = [i for i in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            e1, e2 = enemies[i], enemies[j]
            if nearby(e1, e2): union(i,j)
    for i in range(N): find(i)
    print(len(set(parent)))
