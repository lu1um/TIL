from itertools import combinations

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
foods = range(N)
A_lists = combinations(foods, N // 2)

result = 100*20
for A_list in A_lists:
    B_list = list(foods)[:]
    A = 0
    B = 0
    for p in A_list:
        B_list.remove(p)
    for i in A_list:
        for j in A_list:
            A += table[i][j]
    for i in B_list:
        for j in B_list:
            B += table[i][j]
    temp = abs(A - B)
    if temp < result:
        result = temp
print(result)