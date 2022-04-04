import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    roads = dict()
    for _ in range(E):
        s, e, w = map(int, input().split())
        if roads.get(s):
            roads[s].append((e, w))
        else:
            roads[s] = [(e, w)]

    stack = [(0, 0)]
    min_cost = 10*1000000
    while stack:
        start, cost = stack.pop()
        if cost >= min_cost:
            continue
        if start == N:
            min_cost = cost
        ends = roads.get(start)
        if roads.get(start):
            for end in ends:
                stack.append((end[0], cost+end[1]))

    print(f'#{tc} {min_cost}')

