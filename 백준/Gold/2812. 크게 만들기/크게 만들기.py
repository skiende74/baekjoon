N, M = map(int,input().split())
seq = list(map(int, list(input())))

result = []
cnt = 0
for s in seq:
    while cnt<M and result and result[-1] < s:
        result.pop()
        cnt += 1 
    result.append(s)
ans = ''.join(map(str, result))
print(ans[:N-M])