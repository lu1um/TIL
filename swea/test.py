import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    # 보드의 길이,  플레이어가 돌을 놓는 횟수

    board = [[0] * n for _ in range(n)]
    # 기존에 있을 돌 색상 표시해주기
    a = n // 2
    board[a - 1][a - 1] = 2
    board[a - 1][a] = 1
    board[a][a - 1] = 1
    board[a][a] = 2

    # 다음에 넣어야할 돌의 위치가 주어지므로
    # 판단해야 할 것
    # 1. 상하좌우대각의 돌 중 '다른색'이 있는지 + '다른색돌'과 인접하여(같은 방향으로) 내 돌이 있는지 확인한다 = > 그래야 놓을 수 있음

    for idx in range(m):
        x, y, dol = map(int, input().split())  ############이전이랑 방향 바꿈
        x = x - 1
        y = y - 1
        board[x][y] = dol
        # 돌을 놓을 곳을 인풋받고, 보드에서 내 돌 주위 돌들을 확인해본다.
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]:
            stack = []  ## 디버깅하면
            for i in range(1, n):  # a = board//2
                nx, ny = x + dx * i, y + dy * i
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 0:
                        break
                        # 간 곳이 비어있으면 방향 바꾸기 위해 break
                    elif board[nx][ny] != dol:
                        stack.append([nx, ny])
                        continue
                    else:  # 나랑 같은 색이 있어   # 사이의 값들을 같은 색으로 바꿔주기
                        while stack:
                            c, d = stack.pop()
                            board[c][d] = dol
                        break

    # 1 흑돌, 2백돌
    b = 0
    w = 0
    for c in board:
        b += c.count(1)
        w += c.count(2)

    if b == 0 or w == 0:
        print(f'#{tc} {b} {w}')
    else:
        print(f'#{tc} {b} {w}')