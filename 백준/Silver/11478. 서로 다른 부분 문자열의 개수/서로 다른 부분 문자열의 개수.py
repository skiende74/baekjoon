S= input()
N=len(S)
print(len({S[i:j+1]
for i in range(N)
    for j in range(i,N)}))