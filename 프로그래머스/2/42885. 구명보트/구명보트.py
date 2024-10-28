def solution(people, limit):
    cnt = 0
    people = sorted(people,reverse=True)
    
    for i in people:
        total = i
        if total + people[-1] <= limit : people.pop()
        cnt += 1
            
    return cnt