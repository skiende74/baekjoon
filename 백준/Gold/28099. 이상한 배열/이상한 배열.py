import sys
from collections import Counter, defaultdict

input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    
    stack = [] # 오큰수 푸는용도
    Olarge = [N+1]*(N) # 오큰수인덱스
    
    used = defaultdict(list) # 2번이상 등장하는 수들의 인덱스를 저장하는 dict(). used[nums[i]].append(i)
    
    # 2번이상 등장한 숫자들 a_set 에 넣기
    a_set = set(Counter(nums) - Counter(set(nums)))
    
    # used : a_set 에 있는 수들 인덱스보관
    for i in range(N):
        
        # used
        if nums[i] in a_set:
            used[nums[i]].append(i)
        
        # 오큰수
        while stack and nums[i] > nums[stack[-1]]:
            Olarge[stack.pop()] = i
        stack.append(i)
    
    # 답찾아내기
    ans = True
    for i in range(N):
        if nums[i] in used and Olarge[i] < used[nums[i]][-1]:
            ans = False
            break
    print( 'Yes' if ans else 'No')