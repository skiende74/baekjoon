#from itertools import acummulate

N, K = map(int, input().split())
A = [0, *map(int, input().split())]
A_cum = [0]*(N+1)
for i in range(1,N+1):
    A_cum[i] = (A_cum[i-1] + A[i]) % K

count = 0
B = [0]*(int(1e3)+1)
for i in range(N+1):
    B[A_cum[i]] += 1

for b in B:
    if b>1:
        count += (b*(b-1))//2
print(count)