def permutation(N, M, i, visited, ls):
    if i == M:
        print(*ls)
        return
    tmp = 0
    for j in range(len(N)):
        if tmp != N[j] and visited[j] == 0:
            tmp = N[j]
            visited[j] = 1
            permutation(N, M, i+1, visited, ls+[N[j]])
            visited[j] = 0

N, M = map(int, input().split())
inp = sorted(list(map(int, input().split())))
permutation(inp, M, 0, [0]*N, [])