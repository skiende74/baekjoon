N = int(input())
seq = list(map(int,input().split()))

M = max(seq)
print(sum(seq)+min(sum(seq)-M+1, M)-M)