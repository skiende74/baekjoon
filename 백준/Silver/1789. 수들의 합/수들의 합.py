S = int(input())

total = 0
for i in range(100000):
    total += i
    if total>S: break
print(i-1)