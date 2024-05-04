cans = ['aya','ye','ma','woo']    

def solution(babbling):
    answer = 0
    for b in babbling:    
        temp = 0
        for can in cans:
            if can in b:
                i = b.find(can)
                temp += len(can)
        if len(b) == temp: answer+=1            
                
    return answer