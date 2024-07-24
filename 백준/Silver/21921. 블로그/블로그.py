N, X = map(int,input().split())
seq = list(map(int,input().split()))
answer = sum(seq[:X])
p = answer
cnt = 1
for i in range(X, N):
    p += seq[i] - seq[i-X]
    if answer < p:
        answer = p
        cnt = 1
    elif answer == p:
        cnt += 1
print(answer if answer else 'SAD')
if answer>0: print(cnt)