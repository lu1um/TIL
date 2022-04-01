import sys
sys.stdin = open('input.txt')

def solve(team, i, start):
    global min_sub
    if i == N:
        return
    elif i == N//2:
        teamA = list()
        teamB = list()
        abilityA = 0
        abilityB = 0
        for idx in range(N):
            t = team[idx]
            if t:
                teamA.append(idx)
            else:
                teamB.append(idx)
        for row in teamA:
            for col in teamA:
                abilityA += arr[row][col]
        for row in teamB:
            for col in teamB:
                abilityB += arr[row][col]
        sub = abs(abilityA - abilityB)
        if sub < min_sub:
            min_sub = sub
    else:
        for j in range(start, N):
            team[j] = 1
            solve(team, i+1, j+1)
            team[j] = 0
            solve(team, i, j+1)
    return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_sub = 100*10
solve(list(range(N)), 0, 0)
print(min_sub)