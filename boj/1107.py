import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
disable = []
if M:
    disable = input().split()  # 6 7 8

up = N
down = N
click = 0
while up != 100 and down != 100:
    isFind = False
    for u in str(up):   # 5459
        if u in disable:    # 5 4 5 9
            break
    else:
        click += len(str(up))
        isFind = True
    for d in str(down):     # '5''4''5''5'
        if d in disable:
            break
    else:
        click += len(str(down))
        isFind = True
    if isFind:
        break   # 반례가 뭐야!!!!!
    up += 1     # 5459
    down -= 1   # 5455
    click += 1
print(click)