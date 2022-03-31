import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, *stations = map(int, input().split())

    bus = 0
    counter = 0
    while True:
        battery = stations[bus]
        charge = 0
        stop = 0
        if bus + battery >= N-1:
            break
        for i in range(1, battery+1):
            if stations[bus+i] + i > charge:
                charge = stations[bus+i] + i
                stop = bus + i
        bus = stop
        counter += 1
    print(f'#{tc} {counter}')

