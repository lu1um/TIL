def permutation(N, M, i, visited, ls):
    if i == M:
        lst.append(ls)
        return
    for j in range(len(N)):
        if visited[j] == 0:
            visited[j] = 1
            permutation(N, M, i+1, visited, ls+[N[j]])
            visited[j] = 0

N, M = map(int, input().split())
lst = []
permutation(range(1, N+1), M, 0, [0]*N, [])
for value in lst:
    print(*value)