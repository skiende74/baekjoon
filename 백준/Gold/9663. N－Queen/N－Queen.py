N = int(input())
hori = [False]*N
diag1 = [False]*(2*N-1)
diag2 = [False]*(2*N-1)

def check(i,j):
    hori[j], diag1[i+j], diag2[N-1-i+j] = True,True,True
def un_check(i,j):
    hori[j], diag1[i+j], diag2[N-1-i+j] = False,False,False

ans = 0
def dfs(i):
    global ans
    if i == N-1: 
        ans += 1
        return
    
    i2=i+1
    for j2 in range(N):
        if hori[j2] or diag1[i2+j2] or diag2[N-1-i2+j2]: continue
        
        check(i2,j2)
        dfs(i2)
        un_check(i2,j2)
dfs(-1)
print(ans)
