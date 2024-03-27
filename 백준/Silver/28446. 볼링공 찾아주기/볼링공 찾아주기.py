import sys
input = sys.stdin.readline
N = int(input())
commands = [list(map(int,input().split())) for _ in range(N)]

where = {}
for command in commands:
    com = command[0]
    if com == 1:
        num, w = command[1:]
        where[w] = num
    else:
        w = command[1]
        print(where[w])