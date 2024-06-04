goal, N = map(int,input().split())
seq = [list(map(int,input().split())) for _ in range(N)]

p1 = min(list(map(lambda x: x[0], seq)))
p2 = min(list(map(lambda x: x[1], seq)))

print(min(p1*(goal//6+1),p1*(goal//6)+p2*(goal%6), p2*goal))