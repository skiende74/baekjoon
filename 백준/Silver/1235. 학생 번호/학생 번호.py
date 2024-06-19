N = int(input())
seq = [input() for _ in range(N)]

i=1
while not len({s[-i:] for s in seq})==N: i+=1
print(i)