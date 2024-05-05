import sys
input = sys.stdin.readline
def union(i,j):
    r1,r2 = find(i),find(j)
    parent[r1] = min(r1,r2)
    parent[r2] = min(r1,r2)
def find(i):
    if parent[i]==i: return i
    parent[i] = find(parent[i])
    return parent[i]
t=1
while True:
    V, E = map(int,input().split())
    if (V,E) == (0,0): break
    
    parent = [i for i in range(V+1)]
    for _ in range(E):
        i,j = map(int,input().split())
        if find(i) == find(j): union(i,0)
        union(i,j)

    for i in range(1,V+1): find(i)
        
    ans = len(set(parent))-1
    print(f'Case {t}: ',end='')
    if ans==0: print('No trees.')
    elif ans==1: print('There is one tree.')
    else: print(f'A forest of {ans} trees.')
    t+=1