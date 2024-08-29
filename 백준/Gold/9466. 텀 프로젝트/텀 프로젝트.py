import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+2)
def find_teamless_students(n, selections):
    visited = [0] * (n + 1)  # 방문 여부를 체크하기 위한 리스트
    finished = [0] * (n + 1)  # 팀 결정 여부 체크
    result = 0

    def dfs(student):
        nonlocal result
        current = student
        path = []

        while not visited[current]:
            visited[current] = 1
            path.append(current)
            current = selections[current - 1]

        if current in path:  # 사이클이 형성된 경우
            result += len(path[path.index(current):])  # 사이클의 길이만큼 결과에 더하기

        for node in path:
            finished[node] = 1  # 경로에 있는 모든 노드를 팀 결정으로 표시

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    return n - result

for _ in range(int(input())):
    N = int(input())
    seq = list(map(int,input().split()))
    print(find_teamless_students(N, seq))