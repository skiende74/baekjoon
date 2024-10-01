from bisect import bisect_left
import sys
input = lambda: sys.stdin.readline().rstrip()
N, Q = map(int,input().split())

names, values = [], []

for _ in range(N):
    n, v = input().split()
    names.append(n)
    values.append(int(v))

for _ in range(Q):
    n = names[0]
    v = int(input())

    l = bisect_left(values, v)
    print(names[l] if v <= values[l] else names[l+1])