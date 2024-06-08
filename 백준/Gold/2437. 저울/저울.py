N = int(input())
weights = sorted(list(map(int,input().split())))
possible = 0
for w in weights:
    if w>possible+1: break
    possible += w
print(possible+1)