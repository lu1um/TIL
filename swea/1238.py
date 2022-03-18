import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, start = map(int, input().split())
    data_lst = input().split()
    graph = dict()
    for i in range(N//2):
        key, value = int(data_lst[i*2]), int(data_lst[i*2+1])
        if graph.get(key):
            graph.get(key).append(value)
        else:
            graph.update({ key: [value] })

    visited = list()
    queue = [start]
    touch = int()
    max_call = 0
    while queue:
        isFirst = True
        next_queue = list()
        while queue:
            touch = queue.pop()
            if touch not in visited:
                if isFirst:
                    isFirst = False
                    max_call = 0
                if touch > max_call:
                    max_call = touch
                visited.append(touch)
                tmp = graph.get(touch)
                if tmp:
                    next_queue.extend(tmp)
        queue = next_queue[:]
    print(f'#{tc} {max_call}')
