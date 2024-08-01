def recursive(N, K):
    if N == 1 and (K==1 or K==3): 
        print('-', end='')
        return
    if K == 2: 
        print(' '*(3**(N-1)), end='')
        return
    recursive(N-1, 1)
    recursive(N-1, 2)
    recursive(N-1, 3)

import sys
lines = list(map(int, sys.stdin.read().split()))
for n in lines:
    recursive(n+1, 1)
    print()