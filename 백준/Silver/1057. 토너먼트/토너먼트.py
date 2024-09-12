from math import log2


N, a, b= map(int,input().split())
for i in range(1, int(N)+1):
    if (a-1)//(2**i) == (b-1)//(2**i): 
        print(i)
        break