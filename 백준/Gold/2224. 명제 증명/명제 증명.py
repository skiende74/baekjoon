from collections import defaultdict
E = int(input())
count = 0

graph = defaultdict(lambda: defaultdict(lambda: 0))
nodes = set()
answers = set()
for _ in range(E):
    a, b = input().split(' => ')
    graph[a][b] = 1
    nodes.add(a)
    nodes.add(b)
    answers.add((a,b))

for k in nodes:
    for i in nodes:
        for j in nodes:
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                answers.add((i,j))

answers = list(filter(lambda x: x[0]!=x[1], answers))
def show(tup): return ' => '.join(tup)
print(len(answers), *map(show, sorted(answers)),sep='\n')