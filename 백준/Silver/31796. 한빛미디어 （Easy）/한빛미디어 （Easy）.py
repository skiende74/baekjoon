N = int(input())
seq = list(map(int, input().split()))
seq.sort()
prev = seq[-1]
count = 1
for s in seq[-2::-1]:
    if s*2<=prev:
        prev = s
        count += 1
print(count)