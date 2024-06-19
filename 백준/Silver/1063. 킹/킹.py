def dirs(com):
    res = [0,0]
    if com[0] == 'L': res[1] = -1
    elif com[0] == 'R': res[1] = 1
    
    if len(com) == 2: com = com[1]
    if com == 'T': res[0] = 1
    elif com == 'B': res[0] = -1
    return res

def get_idx(pose):
    j = ord(pose[0])-ord('A')
    i = ord(pose[1])-ord('1')
    return i,j
def get_pose(i,j):
    j = chr(j+ord('A'))
    i = f'{i+1}'
    return j+i

king, stone, M = input().split()
i, j = get_idx(king)
i_, j_ = get_idx(stone)

for _ in range(int(M)):
    di, dj = dirs(input())
    i2, j2 = i+di, j+dj
    if not(0<=i2<8 and 0<=j2<8): continue
    if (i2,j2) == (i_,j_): 
        if not(0<=i_+di<8 and 0<=j_+dj<8): continue
        i_, j_ = i_+di, j_+dj
    i, j = i2, j2
    
print(get_pose(i, j))
print(get_pose(i_, j_))
       