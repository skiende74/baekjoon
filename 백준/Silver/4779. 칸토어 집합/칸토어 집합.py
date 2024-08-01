def recursive(N):
    if N == 0: return '-'
    p = recursive(N-1)
    return p + ' '*(3**(N-1)) + p
    
import sys
lines = list(map(int, sys.stdin.read().split()))
for n in lines:
    print(recursive(n))
    