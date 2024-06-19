N = int(input())
seq = [input() for _ in range(N)]

possible = lambda k: len(set(map(lambda x: x[-k:], seq)))==N

for i in range(1, len(seq[0])+1):
    if possible(i): break
print(i)