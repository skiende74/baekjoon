N = int(input())
seq = list(map(int,input().split()))
dp_l = [1]*N
dp_r = [1]*N
for i in range(1, N):
    for j in range(i):
        if seq[j] > seq[i]:
            dp_l[i] = max(dp_l[i], dp_l[j]+1)
for i in range(N-1)[::-1]:
    for j in range(i,N):
        if seq[j] > seq[i]:
            dp_r[i] = max(dp_r[i], dp_r[j]+1)

l = [0]*N
print(max([dp_l[i] + dp_r[i] for i in range(1,N)] if N>1 else [2])-1)