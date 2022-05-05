def solution(str1, str2):
    pre = ''
    group1 = dict()
    for s in str1.lower():
        if s.isalpha():
            if pre:
                txt = pre + s
                if group1.get(txt):
                    group1[txt] += 1
                else:
                    group1[txt] = 1
            pre = s
        else:
            pre = ''
    pre = ''
    group2 = dict()
    for s in str2.lower():
        if s.isalpha():
            if pre:
                txt = pre + s
                if group2.get(txt):
                    group2[txt] += 1
                else:
                    group2[txt] = 1
            pre = s
        else:
            pre = ''

    cross = 0
    union = 0
    cross_group = []
    for key in group1.keys():
        if group2.get(key):
            cross += min(group1[key], group2[key])
            union += max(group1[key], group2[key])
            cross_group.append(key)
        else:
            union += group1[key]
    for key in group2.keys():
        if key not in cross_group:
            union += group2[key]
    if union:
        answer = int(cross/union * 65536)
    else:
        answer = 65536
    return answer

print(solution('FRANCE', 'french'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('handshake', 'shake hands'))