import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
words = [input() for _ in range(N)]

class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}

root = Trie()
def add(word):
    t = root
    for w in word:
        if w not in t.children: t.children[w] = Trie()    
        t = t.children[w]
    t.is_end = True        

for word in words:
    add(word)

get_score = [0,0,0,1,1,2,3,5,11]
def get_scores(ans_set):
    return sum([ get_score[len(ans)] for ans in ans_set])

def dfs(i,j, t):
    global ans
    if t.is_end: ans_set.add(ans)
    if len(ans)>=8: return

    for di, dj in zip([0,0,-1,1,-1,-1,1,1], [-1,1,0,0,-1,1,-1,1]):
        i2,j2 = i+di, j+dj
        if not(0<=i2<4 and 0<=j2<4): continue
        if grid[i2][j2] not in t.children: continue
        if visited[i2][j2]: continue

        visited[i2][j2] = True
        ans += grid[i2][j2]
        dfs(i2, j2, t.children[grid[i2][j2]])
        visited[i2][j2] = False
        ans = ans[:-1]
input()
Q = int(input())
for l in range(Q):
    grid = [list(input()) for _ in range(4)]
    if l<Q-1: input()

    ans_set = set()
    for i0 in range(4):
        for j0 in range(4):
            if grid[i0][j0] not in root.children: continue
            visited = [[False]*4 for _ in range(4)]
            visited[i0][j0] = True
            ans = grid[i0][j0]

            dfs(i0,j0, root.children[grid[i0][j0]])
    
    M = max(map(len, ans_set))
    print(get_scores(ans_set), sorted( filter(lambda x: len(x) == M, ans_set))[0], len(ans_set))