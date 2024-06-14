N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort()
cnt = 0
exist = []
if cranes[0]<boxes[-1]: print(-1)
else:
    while boxes:
        for c in cranes:
            if not boxes: break
            j = len(boxes)-1
            while j>=0 and c < boxes[j]: j -= 1
            if j>-1: boxes.pop(j)
        cnt+=1
    print(cnt)