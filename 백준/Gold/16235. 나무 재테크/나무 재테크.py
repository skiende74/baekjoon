from collections import deque
N, Q, K = map(int,input().split())
grid = [[5]*N for _ in range(N)]
supply = [list(map(int,input().split())) for _ in range(N)]
tree = [[deque([]) for _ in range(N)] for _ in range(N)]
dead = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(Q):
    i,j, z = map(int,input().split())
    tree[i-1][j-1].append(z)

def spring():
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for idx, t in enumerate(tree[i][j]):
                    if grid[i][j] >= t:
                        grid[i][j] -= t
                        tree[i][j][idx] += 1
                    else:
                        dead[i][j] = list(tree[i][j])[idx:]
                        tree[i][j] = deque(list(tree[i][j])[:idx])
                        break 
def summer():
    for i in range(N):
        for j in range(N):
            if not dead[i][j]: continue 
            grid[i][j] += sum(map(lambda x: x//2, dead[i][j]))
            dead[i][j] = []

def fall():
    for i in range(N):
        for j in range(N):
            
            for t in tree[i][j]:
                if t % 5 != 0: continue
                for di, dj in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]): 
                    i2,j2 = i+di, j+dj
                    if not(0<=i2<N and 0<=j2<N): continue
                    tree[i2][j2].appendleft(1)
def winter():
    for i in range(N):
        for j in range(N):
            grid[i][j] += supply[i][j]

for _ in range(K):
    spring()
    summer()
    fall()
    winter()

print(sum(
    [
    len(tree[i][j])
        for i in range(N)
            for j in range(N)
    ]))