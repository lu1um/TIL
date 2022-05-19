HEX = '0123456789ABCDEF'

def solution(n, t, m, p):
    answer = ''
    turn = 1
    num = 0
    while len(answer) < t:
        deci = num
        res = list()
        while deci >= n:
            a = deci % n
            deci //= n
            res.append(a)
        res.append(deci)
        for r in res[::-1]:
            if turn == p:
                temp = HEX[r]
                answer += temp
            turn += 1
            if turn > m:
                turn = 1
        num += 1
    return answer[:t]



print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))