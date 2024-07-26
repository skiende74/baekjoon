
from math import ceil, log2

def build(node, s, e):
    if s == e:
        tree[node] = seq[s]
        return

    m = (s + e) // 2
    build(node*2, s, m)
    build(node*2+1, m+1, e)
    tree[node] = tree[node*2] + tree[node*2 + 1]

def update(node, s, e, i, val):
    if i < s or e < i: return
    if s == e:
        tree[node] = val
        return
    m = (s + e) // 2
    update(node*2, s, m, i , val)
    update(node*2+1, m+1, e, i , val)
    tree[node] = tree[node*2] + tree[node*2 + 1]

def query(node, s, e, i, j):
    if j < s or e < i: return 0
    if i <= s and e <= j: return tree[node]

    m = (s+e) // 2
    return query(node*2, s, m, i, j) + query(node*2 + 1, m+1, e, i, j)

import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
seq = [0] + [int(input()) for _ in range(N)]
L = 1 << (ceil(log2(N))+1)
tree = [0] * L
build(1, 1, N)
for _ in range(M+K):
    op, i, j = map(int, input().split())
    if op == 1: update(1, 1, N, i, j)
    elif op == 2: print(query(1, 1, N, i, j))