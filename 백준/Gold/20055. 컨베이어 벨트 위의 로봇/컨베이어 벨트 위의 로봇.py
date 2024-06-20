N, K = map(int,input().split())
seq = list(map(int,input().split()))
robots = [0]*N
def rotate():
    global seq
    seq = [seq[-1]] + seq[:-1]
def rotate_robot():
    global robots
    robots = [0] + robots[:-2] + [0]
def move():
    for i in range(N-1)[::-1]:
        if seq[i+1] > 0 and robots[i] and not robots[i+1]:
            robots[i+1] = 1
            robots[i] = 0
            seq[i+1] -= 1
def load_robot():
    if seq[0]>0:
        robots[0] = 1
        seq[0] -= 1

def is_playing():
    return len(list(filter(lambda x: x==0, seq)))<K

cnt = 0
while True:
    rotate()
    rotate_robot()
    move()
    load_robot()
    cnt += 1
    if not is_playing(): break
print(cnt)