import sys
input = sys.stdin.readline

T = int(input())

def solve():
    V, E = map(int,input().split())

    INF = 10**9
    grid = [[INF]*(V+1) for _ in range(V+1)]
    for i in range(1,V+1): grid[i][i] = 0
    for _ in range(E):
        i,j,w = map(int,input().split())
        grid[i][j] = w
        grid[j][i] = w

    for k in range(1,V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])
    
    K = int(input())
    ends = list(map(int,input().split()))
    min_dist = INF
    answers= []
    for s in range(1,V+1):
        dist=sum([grid[s][e] for e in ends])
        min_dist = min(min_dist, dist)
    for s in range(1,V+1):
        dist=sum([grid[s][e] for e in ends])
        if min_dist == dist:
            answers.append(s)
    print(sorted(answers)[0])
for _ in range(T): solve()