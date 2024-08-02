def dfs1(i):
    if i == '.': return
    print(i, end='')
    dfs1(graph[i][0])
    dfs1(graph[i][1])

def dfs2(i):
    if i == '.': return
    dfs2(graph[i][0])
    print(i, end='')
    dfs2(graph[i][1])

def dfs3(i):
    if i == '.': return
    dfs3(graph[i][0])
    dfs3(graph[i][1])
    print(i, end='')

graph = {'.':[]}
N = int(input())
for _ in range(N):
    i, j , k = input().split()
    graph[i] = [j,k]

dfs1('A')
print()
dfs2('A')
print()
dfs3('A')
print()
