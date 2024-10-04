def solution(users, emoticons):
    results=[]
    def dfs(discounts):
        if len(discounts)==7:
            return calc(discounts)
        return max( [ dfs([*discounts, r]) for r in [10,20,30,40] ] )
    
    def calc(discounts):
        result = [0, 0]
        for rate, money in users:
            sales = 0
            for price, discount in zip(emoticons, discounts):
                if discount >= rate:  sales += price*(1-discount*0.01)
            if sales >= money:  result[0] += 1
            else:  result[1] += sales
                    
        return result
    return dfs([])
    