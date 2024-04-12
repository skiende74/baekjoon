from itertools import accumulate
from collections import Counter

def count(seq):
    acm = list(accumulate([0]+seq))
    return Counter([acm[j]-acm[i] 
            for i in range(len(seq)+1)
            for j in range(i+1, len(seq)+1)])

S = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

Ac = count(A)
Bc = count(B)
ans = 0
for a, c in Ac.items():
    ans += c*Bc[S-a]
print(ans)