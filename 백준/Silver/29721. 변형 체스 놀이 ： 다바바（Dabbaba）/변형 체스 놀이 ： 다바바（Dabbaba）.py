import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dababas = {tuple(map(int,input().split())) for _ in range(K)}

answers = set()
for i, j in dababas:
    for di, dj in zip([0,0,-2,2],[-2,2,0,0]):
        i2, j2 = i+di, j+dj
        if 1<=i2<=N and 1<=j2<=N and (i2,j2) not in dababas:
            answers.add((i2, j2))
print(len(answers))