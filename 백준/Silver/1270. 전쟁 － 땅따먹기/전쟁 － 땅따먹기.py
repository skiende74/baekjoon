
from collections import Counter

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, *seq = map(int,input().split())
    counter = Counter(seq)
    c = counter.most_common(1)[0]
    
    print(c[0] if c[1]>N//2 else 'SYJKGW')