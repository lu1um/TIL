import sys
sys.stdin = open('input.txt')

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, K = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

stack = list()
while S:
    for virus_num in range(1, K+1):
        for i in range(N):
            for j in range(N):
                if plate[i][j] == virus_num:
                    for d in DELTA:
                        di = i + d[0]
                        dj = j + d[1]
                        if 0<=di<N and 0<=dj<N:
                            if plate[di][dj] == 0:
                                stack.append((di, dj, virus_num))
    while stack:
        i, j, virus = stack.pop()
        plate[i][j] = virus
    S -= 1
print(plate[X-1][Y-1])