import sys

input = sys.stdin.readline

def solution():
    while 1:
        n, m = input().split()
        n, m = int(n), int(float(m)*100+0.5)
        if n == m == 0:
            break
        temp = []
        for _ in range(n):
            c, p = input().split()
            c, p = int(c), int(float(p)*100+0.5)
            temp.append((c, p))
        temp.sort()
        candies = [temp[0]]
        for i in range(1, n):
            if temp[i][0] > candies[-1][0]:
                candies.append(temp[i])
        dp = [0]*(m+1)
        for c, p in candies:
            for i in range(p, m+1):
                cnt = dp[i-p]+c
                if cnt > dp[i]:
                    dp[i] = cnt
        print(dp[-1])

solution()