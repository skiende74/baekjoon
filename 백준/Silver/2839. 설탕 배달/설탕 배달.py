rem={0:0,1:1,2:2,3:1,4:2}
N=int(input())
if N in [4,7]:
    print(-1)
else:
    print(N//5+rem[N%5])