T=1
while True:
    N = int(input())
    if N == 0: break
    parent = [i for i in range(N)]
    def union(i,j):
        if find(i) == find(j): return
        r = min(find(i), find(j))
        parent[i] = r
        parent[j] = r

    def find(i):
        if parent[i] == parent[parent[i]]: return parent[i]
        parent[i] = find(parent[i])
        return parent[i]

    people=[]
    i=-1
    for _ in range(N):
        a, b = input().split()
        
        if a not in people:
            people.append(a)
            i+=1
            ai = i
        if b not in people:
            people.append(b)
            i+=1
            bi = i
        union(ai,bi)
    print(T, len(set(parent)))
    T += 1