
def build(node, s, e):
    if s == e:
        tree[node] = seq[s]
        return
    
    m = (s + e) // 2
    build(node*2, s, m)
    build(node*2+1, m+1, e)
    tree[node] = min(tree[node*2], tree[node*2 + 1])

def query(node, s, e, i, j):
    if j < s or e < i: return 10**9
    if i <= s and e <= j: return tree[node]

    m = (s + e) // 2
    return min(query(node*2, s, m, i, j), query(node*2 + 1, m+1, e, i, j))

from math import ceil, log2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = [0]+[int(input()) for _ in range(N)]
L = 1 << ceil(log2(N))+1
tree = [0]*L

build(1,1,N)
for _ in range(M):
    i, j = map(int,input().split())
    print(query(1, 1, N, i, j))