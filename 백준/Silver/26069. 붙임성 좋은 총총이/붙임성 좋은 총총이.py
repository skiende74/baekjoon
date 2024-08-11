import sys
input = lambda: sys.stdin.readline().rstrip()
my_set = set(['ChongChong'])
N = int(input())
for _ in range(N):
    a, b = input().split()
    if a in my_set or b in my_set:
        my_set.add(a)
        my_set.add(b)
print(len(my_set))