import sys
input=sys.stdin.readline


N,K=map(int,input().split())
L=list(map(int,input().split()))

start=1 ; end=1000000000000000000

while start<=end:
    mid=(start+end)//2
    total = 0
    for i in range(1,N):
        if mid-(L[i]-L[i-1]-1)>=0:
            m = mid
            n=mid-(L[i]-L[i-1]-1)
            S=(n+m)*(m-n+1)//2
            total += S
        else:
            S=mid*(mid+1)//2
            total +=S
    total+=mid*(mid+1)//2
    if total>=K:
        end=mid-1
    else:
        start=mid+1

print(start)