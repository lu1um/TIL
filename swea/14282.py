import sys
sys.stdin = open('input.txt')
# failed

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i, j, fuel, visited):
    global min_fuel
    if fuel > min_fuel:
        return
    if i == N-1 and j == N-1:
        min_fuel = fuel
        return
    for d in DELTA:
        di = i + d[0]
        dj = j + d[1]
        if 0<=di<N and 0<=dj<N and (di, dj) not in visited:
            if arr[di][dj] > arr[i][j]:
                _fuel = fuel + arr[di][dj]-arr[i][j] + 1
            else:
                _fuel = fuel + 1
            dfs(di, dj, _fuel, visited+[(di, dj)])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_fuel = float('inf')
    dfs(0, 0, 0, [])
    print(f'#{tc} {min_fuel}')

