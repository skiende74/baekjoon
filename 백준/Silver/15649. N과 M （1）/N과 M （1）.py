n, m = map(int,input().split())
check=[0 for i in range(n+1)]

def permultation(now,m,s):
    if (now==m):
        print(s)
    else:
        for i in range(1,n+1):
            if check[i]==0:
                    check[i]=1
                    permultation(now+1,m,s+str(i)+' ')
                    check[i]=0

permultation(0,m,"")