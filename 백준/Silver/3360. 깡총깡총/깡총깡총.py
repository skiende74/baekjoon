N = int(input())
Q = 1000000

def get(N):
    N, rem = divmod(N,6)
    X = 6*((N*(N+1))//2)%Q
    a = [-3*N, -2*N, -N, 1, N+1, 2*N+2]
    return a[rem]+X

print((get(N)%Q + N//2+1)%Q)
