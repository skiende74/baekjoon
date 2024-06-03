T = int(input())


def union(i,j):
    pi,pj = find(i), find(j)
    px, py  = min(pi,pj), max(pi,pj)
    parent[py] = px
    if px==py: return
    length[px] += length[py]
    length[py] = 0

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

for _ in range(T):
    N, Seed, A, B = map(int, input().split())
    visited = set()
    parent = [i for i in range(N)]
    length = [1]*N
    E = Seed % N**2
    X = E//N
    Y = E % N    
    visited.add(E)
    union(X,Y)
    ans = 0
    for i in range(1,10**6):
        if length[0] == N: 
            ans = i
            break    
        E = (E*A+B) % N**2
        X = E//N
        Y = E % N
        # if A==9: print(E, length)
        if E in visited: break
        visited.add(E)
        union(X,Y)
    print(ans)
