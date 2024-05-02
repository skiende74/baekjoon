import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    Q = int(input())

    people = dict()
    queries = [input().split() for _ in range(Q)]
    i = 0
    for q1,q2 in queries:
        if q1 not in people:
            people[q1]=i
            i += 1
        if q2 not in people:
            people[q2]=i
            i += 1
    N=i

    parent = [i for i in range(N)]
    def union(i,j):
        r1,r2 = find(i),find(j)
        r,s = min(r1,r2), max(r1,r2)
        if r==s: return
        parent[s] = r
        counter[r],counter[s] = counter[r] + counter[s],0
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    counter = [1]*N
    for q1, q2 in queries:
        q1, q2 = people[q1], people[q2]
        r1, r2 = find(q1), find(q2)
        union(q1,q2)
        print(counter[min(r1,r2)])