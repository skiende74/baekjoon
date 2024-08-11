import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
my_set = set()
ans = 0
for _ in range(N):
    S = input()
    if S == 'ENTER':
        ans += len(my_set)
        my_set.clear()
        continue
    my_set.add(S)
print(ans+len(my_set))