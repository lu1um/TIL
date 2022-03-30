import sys
sys.stdin = open('input.txt')

N = int(input())
crains = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

if boxes[0] > crains[0]:
    print(-1)
else:
    time = 0
    while boxes:
        for crain in crains:
            for box in boxes:
                if box <= crain:
                    boxes.remove(box)
                    break
        time += 1

    print(time)