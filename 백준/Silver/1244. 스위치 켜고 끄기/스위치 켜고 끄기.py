N = int(input())
seq = list(map(int,input().split()))
Q = int(input())
for _ in range(Q):
    s, num = map(int,input().split())
    num-=1
    if s == 1:
        for i in range(num, N, num+1): seq[i] = 1-seq[i]
    else:
        d = min(num, N-1-num)
        D = 0
        for di in range(1, d+1):
            if seq[num+di] == seq[num-di] and D==di-1: D = di
        for i in range(num-D, num+D+1): seq[i] = 1-seq[i]

for i in range((N-1)//20+1):
    print(' '.join(map(str, seq[i*20:i*20+20])))