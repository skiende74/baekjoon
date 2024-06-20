
def rotate_rev(wheel): return wheel[1:]+[wheel[0]]
def rotate(wheel): return [wheel[-1]]+wheel[:-1]

def dfs(i):
    j = i+1
    if 0<=j<4 and not visited[j]:
        visited[j] = True
        if wheels[i][2] != wheels[j][-2]: 
            nums.append(j)
            dfs(j)
    j = i-1
    if 0<=j<4 and not visited[j]:
        visited[j] = True
        if wheels[i][-2] != wheels[j][2]: 
            nums.append(j)
            dfs(j)
N = 8
wheels = [list(map(int, list(input()))) for _ in range(4)]
M = int(input())
for _ in range(M):
    num, dir = map(int, input().split())
    num -= 1
    nums, dirs = [num],[dir]

    visited = [False]*4
    visited[num] = True
    dfs(num)

    for n in nums:
        if dir*(-1)**(n-num)==1: wheels[n] = rotate(wheels[n])
        else: wheels[n] = rotate_rev(wheels[n])
scores = [1,2,4,8]

print(sum([wheels[i][0]*scores[i] 
for i in range(4)]))