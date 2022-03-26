import sys
sys.stdin = open('input.txt')


DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solve(numbers, mat, stack, i, j, size):
    if size == 7:
        numbers.add(''.join(map(str, stack)))
    else:
        for d in DELTA:
            di = i + d[0]
            dj = j + d[1]
            if 0<=di<4 and 0<=dj<4:
                solve(numbers, mat, stack+[mat[di][dj]], di, dj, size+1)

T = int(input())
for tc in range(1, T+1):
    mat = [list(map(int, input().split())) for _ in range(4)]

    numbers = set()
    for i in range(4):
        for j in range(4):
            stack = [mat[i][j]] + [0] * 6
            solve(numbers, mat, stack, i, j, 1)
    print(f'#{tc} {len(numbers)}')
