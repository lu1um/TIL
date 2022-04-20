N, M, K = map(int, input().split())

teams = 0
while N > 1 and M > 0:
    N -= 2
    M -= 1
    teams += 1

K -= N + M
if K > 0:
    teams -= K // 3
    if K % 3:
        teams -= 1
print(teams)