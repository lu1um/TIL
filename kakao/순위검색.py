def solution(info, query):
    N = len(info)
    participants = [[''] * 5 for _ in range(N)]
    for i in range(N):
        for j, s in enumerate(info[i].split()):
            participants[i][j] = s

    answer = [0] * len(query)
    for idx, qr in enumerate(query):
        candidate = [1] * N
        for i, q in enumerate(qr.split(' and ')):
            if q == '-':
                continue
            if i == 3:
                food, score = q.split()
                if food != '-':
                    for j in range(N):
                        if not candidate[j]:
                            continue
                        if not participants[j][3] == food:
                            candidate[j] = 0
                for j in range(N):
                    if not candidate[j]:
                        continue
                    if int(participants[j][4]) < int(score):
                        candidate[j] = 0
            else:
                for j in range(N):
                    if not candidate[j]:
                        continue
                    if not participants[j][i] == q:
                        candidate[j] = 0
        answer[idx] = sum(candidate)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))