def solution(dartResult):
    idx = 0
    scores = [0, 0, 0]
    for j in range(3):
        score = int(dartResult[idx])
        idx += 1
        if dartResult[idx] == '0':
            score += 9
            idx += 1
        if dartResult[idx] == 'S':
            pass
        elif dartResult[idx] == 'D':
            score = score ** 2
        elif dartResult[idx] == 'T':
            score = score ** 3
        idx += 1
        if idx >= len(dartResult):
            scores[j] = score
            break
        if dartResult[idx] == '*':
            score *= 2
            if j > 0:
                scores[j-1] *= 2
            idx += 1
        elif dartResult[idx] == '#':
            score *= -1
            idx += 1
        scores[j] = score
    answer = sum(scores)
    return answer

print(solution("1D2S#10S"))