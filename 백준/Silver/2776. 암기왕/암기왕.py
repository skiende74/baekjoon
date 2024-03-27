import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    N = int(input())
    seen = set(map(int,input().split()))
    M = int(input())
    said = list(map(int,input().split()))

    answer = list(map(lambda x: '1' if x in seen else '0', said))
    print('\n'.join(answer))   