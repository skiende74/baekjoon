N = int(input())

ans = []
j = 1
for i in range(1, N+1):
    while j<N and j**2 - i**2 < N: j += 1
    if j**2 - i**2 == N: ans.append(j)

print('\n'.join(map(str, ans)) if ans else -1)