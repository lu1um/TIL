import sys
sys.stdin = open('input.txt')

def solver(visited, row, cost):
    global min_cost
    if cost >= min_cost:
        return
    if row == N:
        if cost < min_cost:
            min_cost = cost
            return
    for i in range(N):
        if i not in visited:
            sum_cost =  cost + costs[row][i]
            solver(visited + [i], row+1, sum_cost)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 15*100
    solver([], 0, 0)
    print(f'#{tc} {min_cost}')
