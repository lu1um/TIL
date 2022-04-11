def solution(s):
    origin = list(s)
    length = len(origin)
    min_len = 1001
    for i in range(1, length//2 + 1):
        start = 0
        new = ''
        while start < length-i:
            compare = ''.join(origin[start:start+i])
            same = 1
            start += i
            while s[start:start+i] == compare:
                start += i
                same += 1
            if same > 1:
                new = new + f'{same}' + compare
            else:
                new = new + compare
        if start < length:
            new = new + s[start:]
        if len(new) < min_len:
            min_len = len(new)
    if min_len == 1001:
        min_len = 1
    return min_len

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
