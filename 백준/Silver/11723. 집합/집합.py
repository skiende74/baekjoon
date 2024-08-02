import sys
input = sys.stdin.readline
N = int(input())
my_set = set()
for _ in range(N):
    com = input().split()
    if com[0] == 'add': my_set.add(int(com[1]))
    if com[0] == 'remove' and int(com[1]) in my_set: my_set.remove(int(com[1]))
    if com[0] == 'check': print(1 if int(com[1]) in my_set else 0)
    if com[0] == 'toggle': my_set.remove(int(com[1])) if int(com[1]) in my_set else my_set.add(int(com[1]))
    if com[0] == 'all': my_set = set(range(1,21))
    if com[0] == 'empty': my_set = set()
