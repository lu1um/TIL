import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    binary = [''] * 12
    isOverflow = False
    for i in range(12):
        num *= 2
        if num >= 1:
            num -= 1
            binary[i] = '1'
        else:
            binary[i] = '0'
        if num == 0:
            break
    else:
        isOverflow = True
        print(f'#{tc} overflow')
    if not isOverflow:
        print(f'#{tc} {"".join(binary)}')
