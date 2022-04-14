def solution(p):
    if not p:
        return ''
    w = list(p)
    length = len(w)
    left = 0
    right = 0
    opened = 0
    idx = 0
    while left != right or left == 0 or right == 0 :
        if w[idx] == '(':
            left += 1
            opened += 1
        else:
            right += 1
            if opened:
                opened -=1
        idx += 1
        if idx == length:
            break
    if opened == 0:
        return p[:idx] + solution(p[idx:])
    else:
        u = '(' + solution(p[idx:]) + ')'   # ( + v + )
        for bracket in w[1:idx-1]:
            if bracket == '(':
                u += ')'
            else:
                u += '('
        return u

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))