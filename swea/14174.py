import sys
sys.stdin = open('input.txt')

def permutation(nums, r, pick, output):
    if len(pick) == r:
        output.append(pick)
        return
    for i in range(len(nums)):
        num = nums.pop(i)
        permutation(nums[:], r, pick+[num], output)
        nums.insert(i, num)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    usages = [list(map(int, input().split())) for _ in range(N)]

    cases = list()
    permutation(list(range(1, N)), N-1, [], cases)
    min_usage = 100*10
    for case in cases:
        use = 0
        start = 0
        for end in case + [0]:
            use += usages[start][end]
            start = end
        if use < min_usage:
            min_usage = use
    print(f'#{tc} {min_usage}')