def solution(n, arr1, arr2):
    answer = list()
    for i in range(n):
        row = bin(arr1[i] | arr2[i])
        code = ''
        idx = -1
        while row[idx] != 'b':
            if row[idx] == '1':
                code = '#' + code
            else:
                code = ' ' + code
            idx -= 1
        while len(code) < n:
            code = ' ' + code
        answer.append(code)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))