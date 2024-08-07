import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
ans = set()

for _ in range(N):
    a, b = input().split()
    if b == 'enter': ans.add(a)
    else: ans.remove(a)
print('\n'.join(reversed(sorted(ans))))