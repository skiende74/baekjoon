from bisect import bisect_left
EGG_COUNT, N = map(int,input().split())
seq = [int(input()) for _ in range(N)]
seq.sort()
ans = 0
ans_price = 0
for price in range(1,10**6+1):
    i = bisect_left(seq, price)
    if ans < min(N-i, EGG_COUNT)*price:
        ans = min(N-i, EGG_COUNT)*price
        ans_price = price
print(ans_price, ans)