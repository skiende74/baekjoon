import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
d = dict()
for _ in range(N):
    k,v = input().split()
    d[k] = v
for _ in range(M):
    print(d[input()])