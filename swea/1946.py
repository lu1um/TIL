import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    string = str()
    for _ in range(N):
        Ci, Ki = input().split()
        string += Ci * int(Ki)
    count = 0
    result = str()
    for char in string:
        result += char
        count += 1
        if count == 10:
            print(result)
            count = 0
            result = ''
    print(result)