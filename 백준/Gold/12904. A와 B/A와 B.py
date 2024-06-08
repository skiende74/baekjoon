S = input()
goal = input()

K = len(goal)-len(S)

for _ in range(K):
    if goal[-1] == 'A':
        goal = goal[:-1]
    else:
        goal = goal[:-1]
        goal = goal[::-1]
print(1 if S ==goal else 0)