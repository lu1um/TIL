def backTracking(queen, N, row):
    global case
    if row == N:
        case += 1
        return
    for i in range(N):
        queen[row] = i
        for j in range(row):
            if queen[row] == queen[j] or abs(queen[row]-queen[j]) == abs(row-j):
                break
        else:
            backTracking(queen, N, row+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    queen = [0] * N
    case = 0
    backTracking(queen, N, 0)
    print(f'#{tc} {case}')