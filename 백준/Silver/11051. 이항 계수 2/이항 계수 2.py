import sys
sys.setrecursionlimit(10**4)
N, K = map(int,input().split())

dp = [-1]*1001
dp[0]=1

def factorial(k):
    if dp[k] != -1: return dp[k]
    dp[k] = k*factorial(k-1)
    return dp[k]
def choose(n,k):
    return (factorial(n)//factorial(k)//factorial(n-k))%10007
print(choose(N,K))