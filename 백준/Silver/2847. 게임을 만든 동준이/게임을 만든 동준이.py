N = int(input())
seq = [int(input()) for _ in range(N)]

prev = 10**9
cnt = 0
for s in seq[::-1]:
    if s>prev-1:
        cnt += s-(prev-1)
        s = prev-1
    prev = s
print(cnt)