from collections import deque
c,n = map(int,input().split())
col_dct = {}
name_dct = {}
for _ in range(c):
  col_dct[input()]=1
for _ in range(n):
  name_dct[input()]=1

q = int(input())
for _ in range(q):
  s = input()
  ans = False
  for k in range(max(1,len(s)-1000), min(len(s),1001)):
    if col_dct.get(s[:k]) and name_dct.get(s[k:]):
      ans=True
      break
  if ans:
    print("Yes")
  else:
    print("No")