import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    works = [tuple(map(int, input().split())) for _ in range(N)]

    works.sort(key=lambda x: x[1])
    start, end = works.pop(0)
    result = 1
    while works:
        while works and start < end:
            start, next_end = works.pop(0)
        if start >= end:
            result += 1
            end = next_end
    print(f'#{tc} {result}')