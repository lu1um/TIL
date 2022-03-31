import sys
sys.stdin = open('input.txt')

def perm(lst, N):
    global min_cost


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    cases = permutations(range(N), N)

    min_cost = 15*100
    for case in cases:
        cost = 0
        row = 0
        for col in case:
            cost += costs[row][col]
            row += 1
        if cost < min_cost:
            min_cost = cost
    print(f'#{tc} {min_cost}')
