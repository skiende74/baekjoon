from math import log10


N, K = map(int,input().split())

m = 10**(int(log10(N))+1)
num = N % K
done = False
for i in range(1, K+5):
    if num == 0: 
        done = True
        break
    num = (num*m+N)%K

print(i if done else -1)