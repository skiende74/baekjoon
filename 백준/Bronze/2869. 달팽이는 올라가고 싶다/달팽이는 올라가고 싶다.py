import math
A,B,V = map(int,input().split())
print(  int(math.ceil((V-A)/(A-B)) +1))