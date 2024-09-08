def solution(answers):
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    n = len(answers)
    
    cnt1 = sum([a==ans1[i%len(ans1)] for i, a in enumerate(answers)])
    cnt2 = sum([a==ans2[i%len(ans2)] for i, a in enumerate(answers)])
    cnt3 = sum([a==ans3[i%len(ans3)] for i, a in enumerate(answers)])
    max_cnt = max([cnt1,cnt2,cnt3])
    answer = [i for i,c in [(1,cnt1),(2,cnt2),(3,cnt3)] if c == max_cnt]
    return answer