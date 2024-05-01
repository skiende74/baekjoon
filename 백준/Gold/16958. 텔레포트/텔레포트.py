import sys
input = sys.stdin.readline
V, T = map(int,input().split())
INF = 10**9
cities = [[0,INF,INF]]+[list(map(int,input().split())) for _ in range(V)]

def calc(i,j):
    if i==0 or j==0: return INF
    c1,c2 = cities[i], cities[j]
    result = abs(c1[2]-c2[2])+abs(c1[1]-c2[1])
    if c1[0] == 1 and c2[0] == 1: result = min(result, T)
    return result

dist = [[calc(i,j) for j in range(V+1)] for i in range(V+1)]

def d(i,j):
    if i<=j: return dist[i][j]
    return dist[j][i]
for k in range(1,V+1):
    for i in range(1,V+1):  
        for j in range(i+1,V+1):
            dist[i][j] = min(d(i,j), d(i,k) + d(k,j))


Q = int(input())
queries = [list(map(int,input().split())) for _ in range(Q)]
for q in queries:
    print(d(*q))