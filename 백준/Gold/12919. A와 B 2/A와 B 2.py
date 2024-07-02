def dfs(seq):
    global ans
    if seq == seq1: 
        ans = 1
        return
    if len(seq) == len(seq1): return
    if seq[-1] == 'A': dfs(seq[:-1])
    if seq[0] == 'B': dfs(seq[-1:0:-1])
ans = 0
seq1 = input()
seq2 = input()
dfs(seq2)
print(ans)
