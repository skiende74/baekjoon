# 숫자가 주어짐 (순열)

def dfs():
    if len(result) == M:
        ans.append(' '.join(map(str, result)))
        return
    for j in range(N):
        if seq[j] in result: continue
        result.append(seq[j])
        dfs()
        result.pop()

N, M = map(int,input().split())
seq = list(map(int,input().split()))
ans, result = [], []

seq.sort()
dfs()
print('\n'.join(ans))