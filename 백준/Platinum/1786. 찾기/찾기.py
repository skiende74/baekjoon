text = input()
pat = input()

N, M = len(text), len(pat) 
text = '#'+text
pat = '#' + pat

f = [-1]+[0]*M
j = -1
for i in range(1, M+1):
    while j>=0 and pat[i] != pat[j+1]: j = f[j]
    j += 1
    f[i] = j

ans = []
j = 0
for i in range(1, N+1):
    while j>=0 and text[i] != pat[j+1]: j = f[j]
    j += 1
    if j==M:
        ans.append(i-j+1)
        j=f[j]

print(len(ans))
print(' '.join(map(str,ans)))