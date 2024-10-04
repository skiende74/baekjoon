# 유저, 상품들, 결과.
# 유저당, (상품당, 할인율10/20/30/40)
import sys
sys.setrecursionlimit(10**7)

def dfs(users, emoticons):
    global result_max  
    if len(discounts) == len(emoticons):
        result = [0,0]
        for discount_need, upper_price in users:
            purchase = 0
            for i in range(len(emoticons)):
                purchase += int((100-discounts[i])*0.01*emoticons[i]) if discounts[i] >= discount_need else 0
                
            if purchase >= upper_price: result[0] += 1
            else: result[1] += purchase
        result_max = max(result_max, result)
        return
        
    for j in range(10, 50, 10):
        discounts.append(j)
        dfs(users, emoticons)
        discounts.pop()
    
def solution(users, emoticons):
    global result_max, discounts
    result_max = [0,0]
    discounts = []
    dfs(users, emoticons)
    return result_max