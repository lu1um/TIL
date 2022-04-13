N, K = map(int, input().split())

lst = list(range(1, N+1))
idx = 0
result = list()
while lst:
    length = len(lst)
    if idx >= length:
        idx = 0
    for i in range(K-1):
        idx += 1
        if idx == length:
            idx = 0
    result.append(lst.pop(idx))
print(result.__str__().replace('[', '<').replace(']', '>'))