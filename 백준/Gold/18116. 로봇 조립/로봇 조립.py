def union(i,j):
    i, j = find(i), find(j)
    if i< j:
        cnt[i] += cnt[j]
        parent[j] = parent[i]
    elif j< i:
        cnt[j] += cnt[i]
        parent[i] = parent[j]

def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

import sys
input = sys.stdin.readline

parent = [i for i in range(10**6+1)]
cnt = [1]*(10**6+1)
M = int(input())

for _ in range(M):
    com = input().split()
    if com[0] == 'I':
        union(int(com[1]), int(com[2]))
    else:
        print(cnt[find(int(com[1]))])