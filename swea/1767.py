import sys
sys.stdin = open('input.txt')

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DELTA = [UP, DOWN, LEFT, RIGHT]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    exynos = [list(map(int, input().split())) for _ in range(N)]
    cores = list()
    for i in range(1, N-1):     # 가생이에 있는 코어는 고려할 필요 없음
        for j in range(1, N-1):
            if exynos[i][j]:
                connect = list()
                for d in DELTA:
                    di, dj = d
                    row = i+di
                    col = j+dj
                    length = 1
                    while 0<=row<N and 0<=col<N:
                        if exynos[row][col]:
                            length = 0
                            break
                        row += di
                        col += dj
                        length += 1
                    connect.append(length)
                cores.append([i, j, connect])
    print(cores)


