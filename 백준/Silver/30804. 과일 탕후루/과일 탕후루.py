N = int(input())
seq = list(map(int,input().split()))
counter = [0]*10
j = 0
counter[seq[0]] += 1
num_set = set([seq[0]])
ans = 0
for i in range(N):
    while j+1 < N and (len(num_set) <2 or len(num_set)==2 and seq[j+1] in num_set):
        j += 1
        counter[seq[j]] += 1
        num_set.add(seq[j])
    ans = max(ans, j-i+1)
    counter[seq[i]] -= 1
    if counter[seq[i]] == 0: num_set.remove(seq[i])

print(ans)