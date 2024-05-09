N,M,K = map(int,input().split())

factorial = [1]*201
for i in range(1, 201): factorial[i] = factorial[i-1]*i

def comb(n,r):
    return factorial[n]//factorial[r]//factorial[n-r]

def solve(a, z, k):
    if a==0: return 'z'*z
    if z==0: return 'a'*a
    if k > comb(a+z,z): return -1
    if k > comb(a-1+z,z):
        return 'z'+solve(a,z-1, k-comb(a+z-1,z))
    return 'a'+solve(a-1,z,k)
print(solve(N,M,K))