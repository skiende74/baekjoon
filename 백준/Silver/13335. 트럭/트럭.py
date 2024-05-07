N, L, W = map(int,input().split())
queue = list(map(int,input().split()))

bridge = []
t = 0
weight = 0
while queue or bridge:

    for b in bridge.copy(): #다리위
        if b[0] >=L: #탈출
            weight -= b[1]
            bridge.remove(b)
        else: #전진
            b[0] += 1
    if queue and queue[0]+weight<=W: 
        w = queue.pop(0)
        bridge.append([1, w])
        weight += w
    t+=1
print(t)