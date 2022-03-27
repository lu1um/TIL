import sys
sys.stdin = open('input.txt')

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

OPPOSITE = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}

TYPE = {
    0: [],
    1: [UP, DOWN, LEFT, RIGHT],
    2: [UP, DOWN],
    3: [LEFT, RIGHT],
    4: [UP, RIGHT],
    5: [DOWN, RIGHT],
    6: [DOWN, LEFT],
    7: [UP, LEFT],
}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    stack = [(R, C)]
    L -= 1
    while L:
        for idx in range(len(stack)):
            i, j = stack[idx]
            pipe = tunnel[i][j]
            for direction in TYPE[pipe]:
                di, dj = direction
                ii = i + di
                jj = j + dj
                if 0<=ii<N and 0<=jj<M:
                    if OPPOSITE[direction] in TYPE[tunnel[ii][jj]] and (ii, jj) not in stack:
                        stack.append((ii, jj))
        L -= 1
    print(f'#{tc} {len(stack)}')