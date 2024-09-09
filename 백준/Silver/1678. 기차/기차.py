N, M, P = map(int,input().split())
train = ['']*(60)

NN = 0
for _ in range(N):
    a, *nums, _ = input().split()
    NN += len(nums)
    for num in nums:
        train[int(num)] = a

P %= NN
i = 0
if P == 0: P = NN
for i in range(60):
    if train[(M+i)%60] != '':
        P -= 1
        if P == 0: break
print(train[(M+i)%60])