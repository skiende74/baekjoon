from itertools import combinations
N, M = map(int, input().split())
knows = list(map(int, input().split()))[1:]
parties = [list(map(int, input().split()))[1:] for _ in range(M)]


def find_parent(i):
    if parent[i] != i:
        parent[i] = find_parent(parent[i])
    return parent[i]


def union_parent(i, j):
    i = find_parent(i)
    j = find_parent(j)
    if i < j:
        parent[j] = i
    elif j < i:
        parent[i] = j


parent = {i: i for i in range(1, N+1)}

for party in parties+[knows]:
    for comb in combinations(party, 2):
        union_parent(*comb)

if knows:
    k = find_parent(knows[0])
else:
    k = -1

count = M
for party in parties:
    for person in party:
        if find_parent(person) == k:
            count -= 1
            break
print(count)
