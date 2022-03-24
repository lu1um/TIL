import sys
sys.stdin = open('input.txt')

DELTA = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

cheese[0] = [2] * M
for row in range(1, N-1):
    cheese[row][0] = 2
    cheese[row][-1] = 2
cheese[-1] = [2] * M

isEnd = False
hour = -1
result = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if cheese[i][j] == 1:
            result += 1
while not isEnd:
    isEnd = True
    remain_cheese = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if cheese[i][j] == 0:
                for d in DELTA:
                    if cheese[i+d[0]][j+d[1]] == 2:
                        cheese[i][j] = 2
                        break
    for i in range(N-1, 0, -1):
        for j in range(M-1, 0, -1):
            if cheese[i][j] == 0:
                for d in DELTA:
                    if cheese[i+d[0]][j+d[1]] == 2:
                        cheese[i][j] = 2
                        break

    for i in range(1, N-1):
        for j in range(1, M-1):
            if cheese[i][j] == 1:
                isEnd = False
                for d in DELTA:
                    if cheese[i+d[0]][j+d[1]] == 2:
                        cheese[i][j] = 0
                        break
                else:
                    remain_cheese += 1
    hour += 1
    if remain_cheese:
        result = remain_cheese

print(f'{hour}\n{result}')