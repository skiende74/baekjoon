import sys
input = sys.stdin.readline
Q=int(input())

N = 10**4+1
dp = [0]*(10**4+1)
dp[1:5]=[1,2,3,4]
dp_3 = [0]+[0,0,1]*(N//3+3)
dp_23 = [0]+[0,1,1,1,1]+[0]*(10**4+1)

for i in range(5,10**4+1):
    dp_23[i] = dp_23[i-2]+dp_3[i]
    dp[i] = dp[i-1]+dp_23[i-2]+dp_3[i-3]
for _ in range(Q):
    print(dp[int(input())])