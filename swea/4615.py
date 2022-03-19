import sys
sys.stdin = open('input.txt')
# othello

DELTA = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

def main():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        board = [[0] * N for _ in range(N)]
        board[N//2][N//2] = 2
        board[N//2-1][N//2] = 1
        board[N//2][N//2-1] = 1
        board[N//2-1][N//2-1] = 2
        color_count = { 1:2, 2:2 }
        opposite = int()
        for _ in range(M):
            x, y, color = map(int, input().split())
            x, y = x-1, y-1
            if color == 1:
                opposite = 2    # 백돌
            else:
                opposite = 1    # 흑돌
            board[y][x] = color
            color_count[color] += 1
            for d in DELTA:
                stack = list()
                if validation(N, *[y+d[1], x+d[0]]):
                    if board[y+d[1]][x+d[0]] == opposite:
                        i = 1
                        while board[y+d[1]*i][x+d[0]*i] == opposite:
                            stack.append([x+d[0]*i, y+d[1]*i])
                            if validation(N, *[y+d[1]*(i+1), x+d[0]*(i+1)]):
                                i += 1
                            else:
                                break
                        if board[y+d[1]*i][x+d[0]*i] == color:
                            while stack:
                                xy = stack.pop()
                                board[xy[1]][xy[0]] = color
                                color_count[color] += 1
                                color_count[opposite] -= 1
        print(f'#{tc} {color_count[1]} {color_count[2]}')

def validation(limit, *num):
    for n in num:
        if n >= limit or n < 0:
            return False
    return True

if __name__ == '__main__':
    main()