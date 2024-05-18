N = int(input())
seq = set(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

print('\n'.join(map(lambda x: '1' if x in seq else '0', queries)))
