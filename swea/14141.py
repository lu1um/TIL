import sys
sys.stdin = open('input.txt')

HEX = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15 }

T = int(input())
for tc in range(1, T+1):
    N, string = input().split()
    binary = str()
    for s in string:
        q = ['0'] * 4
        i = 3
        dec = HEX[s]
        while dec > 0:
            q[i] = str(dec % 2)
            dec = dec // 2
            i -= 1
        binary += ''.join(q)
    print(f'#{tc} {binary}')

