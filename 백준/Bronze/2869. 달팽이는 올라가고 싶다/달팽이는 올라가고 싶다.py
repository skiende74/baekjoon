import math
A,B,V = map(int, input().split())
result = V-A
print(math.ceil(result/(A-B))+1)