def solver(arrow, shoot, score, i):
    global max_score

    if i == 11:
        if

def solution(n, info):
    max_score = 0
    answer = []
    for start in range(11):
        temp = [0] * 11
        arrow = n
        score = 0
        for i in range(start, 11):
            shoot = info[i]+1
            if shoot > arrow:
                score -= 10-i
                continue
            else:
                arrow -= shoot
                temp[i] = shoot
                score += 10-i
            if arrow == 0:
                break
        if score >= max_score:
            max_score = score
            answer = temp[:]
    if max_score > 0:
        return answer
    else:
        return [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))