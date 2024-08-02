import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())

set1 = set()
ans = []
for _ in range(N): set1.add(input())
for _ in range(M): 
    name = input()
    if name in set1: ans.append(name)
print(len(ans))
print('\n'.join(sorted(ans)))