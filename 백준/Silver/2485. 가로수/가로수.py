from math import gcd
import sys
input = sys.stdin.readline
N = int(input())
seq = [int(input()) for _ in range(N)]
g = 0
for i in range(N-1):
    g = gcd(g, seq[i+1]-seq[i])
print(sum([ (seq[i+1]-seq[i])//g -1 for i in range(N-1)]))