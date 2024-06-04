import sys
input = sys.stdin.readline
N = int(input())
seq = [list(map(int,input().split())) for _ in range(N)]

seq.sort(key=lambda x: (x[1],x[0]))
e_prev=-1
ans = 0
for s,e in seq:
    if s>= e_prev:
        ans +=1
        e_prev = e
print(ans)    