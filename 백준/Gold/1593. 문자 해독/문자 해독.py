def count_permutations(g, s_len, W, S):
    from collections import Counter

    # 단어 W와 동일한 길이의 초기 윈도우를 설정
    W_counter = Counter(W)
    window_counter = Counter(S[:g])
    
    count = 0
    if W_counter == window_counter:
        count += 1

    for i in range(1, s_len - g + 1):
        # 윈도우를 한 칸 오른쪽으로 이동
        start_char = S[i - 1]
        new_char = S[i + g - 1]

        # 윈도우의 카운터를 업데이트
        window_counter[start_char] -= 1
        if window_counter[start_char] == 0:
            del window_counter[start_char]
        window_counter[new_char] += 1

        # W와 현재 윈도우의 빈도가 일치하는지 확인
        if W_counter == window_counter:
            count += 1

    return count

# 입력 처리
g, s_len = map(int, input().split())
W = input().strip()
S = input().strip()

# 결과 출력
print(count_permutations(g, s_len, W, S))
