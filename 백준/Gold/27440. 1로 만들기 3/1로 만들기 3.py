from collections import deque, defaultdict

visited = defaultdict(lambda:2*10**9)
visited = set()
def bfs():
    while Q:
        i, c = Q.popleft()
        js = []
        if i%2 == 0 and i//2 not in visited: 
            visited.add(i//2)
            js.append(i//2)
        if i%3 == 0 and i//3 not in visited: 
            visited.add(i//3)
            js.append(i//3)
        if i-1 > 0 and i-1 not in visited: 
            visited.add(i-1)
            js.append(i-1)

        for j in js:
            Q.append((j,c+1))
            if j == 1:
                return c+1
n = int(input())
Q = deque([(n, 0)])
if n == 1:
    print(0)
else:
    print(bfs())