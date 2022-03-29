import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cargos = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))

    weight = 0
    for truck in trucks:
        for i in range(len(cargos)-1, -1, -1):
            cargo = cargos[i]
            if cargo <= truck:
                weight += cargo
                del cargos[i]
                break
    print(f'#{tc} {weight}')