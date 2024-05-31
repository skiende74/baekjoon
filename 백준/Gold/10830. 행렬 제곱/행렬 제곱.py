import sys
from copy import deepcopy
input = sys.stdin.readline
N, Mult = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

opers = []
while Mult>1:
    if Mult % 2 == 0:
        Mult //= 2
        opers.append(2)
    else:
        Mult -= 1
        opers.append(1)
opers = opers[::-1]

def mult(mat1,mat2):
    N = len(mat1)
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += mat1[i][k]*mat2[k][j]
            res[i][j] %= 1000
    return res

cur = deepcopy(matrix)
for op in opers:
    if op==1:
        cur = mult(cur, matrix)
    else:
        cur = mult(cur, cur)

for i in range(N):
    for j in range(N):
        print(cur[i][j]%1000, end=' ')
    print()