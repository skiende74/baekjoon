M = int(input())
pat = '#'+input()
f = [-1]+[0]*M
j = -1
for i in range(1,M+1):
    while j>=0 and pat[j+1] != pat[i]: j = f[j]
    j += 1
    f[i] = j
print(M-f[-1])