N, M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

tetros = [[[1,1,1,1]],
          [[1,1],[1,1]],
          [[1,1,1],[1,0,0]],[[1,0,0],[1,1,1]],
          [[0,1,1],[1,1,0]],[[1,1,0],[0,1,1]],
          [[1,1,1],[0,1,0]],[[0,1,0],[1,1,1]]
          ]

def rotate_tetro(tetro):
    n, m = len(tetro), len(tetro[0])
    return [ [tetro[j][m-1-i] for j in range(n)] for i in range(m)]

def get_subgrid(i,j,h,w):
    return [ g[j:j+w] for g in grid[i:i+h]]

def get_sum(sub_grid, tetro):
    n, m = len(sub_grid), len(sub_grid[0])
    return sum([ sub_grid[i][j] for i in range(n) for j in range(m) if tetro[i][j]])

def test():
    max_val = 0
    for tetro in tetros: # 테트로미노
        for _ in range(4): # 4 회전 고려
            tetro = rotate_tetro(tetro)
            n, m = len(tetro), len(tetro[0])
            for i in range(N-n+1):  # 테트로 위치이동
                for j in range(M-m+1):
                    max_val = max(max_val, get_sum(get_subgrid(i,j,n,m),tetro))
    return max_val

print(test())