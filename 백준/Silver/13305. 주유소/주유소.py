N = int(input())
dist = list(map(int,input().split())) +[0]
prices = list(map(int,input().split()))

min_price = 10**9+1
ans = 0
for d,p in zip(dist,prices):
    min_price = min(min_price, p)

    ans+=d*(min_price)
print(ans)