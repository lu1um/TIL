import sys
sys.stdin = open('input.txt')

STATUS_COMING = 0
STATUS_RECEPTION_WAIT = 1
STATUS_RECEPTION = 2
STATUS_REPAIR_WAIT = 3
STATUS_REPAIR = 4
STATUS_END = 5

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    A -= 1
    B -= 1
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    customer = list(map(int, input().split()))
    status = [STATUS_COMING] * K
    result = 0

    visit_A = [False] * K
    rec_occupy = [-1] * N
    rep_occupy = [-1] * M
    rec_waiting = list()
    rep_waiting = list()
    while sum(status) < K * STATUS_END:
        rep_temp = list()
        for i in range(K):
            customer[i] -= 1
            if customer[i] <= 0:
                if status[i] == STATUS_COMING:
                    status[i] += 1
                    rec_waiting.append(i)
                elif status[i] == STATUS_RECEPTION_WAIT:
                    pass
                elif status[i] == STATUS_RECEPTION:
                    status[i] += 1
                    rep_temp.append((rec_occupy.index(i), i))
                    rec_occupy[rec_occupy.index(i)] = -1
                elif status[i] == STATUS_REPAIR_WAIT:
                    pass
                elif status[i] == STATUS_REPAIR:
                    status[i] += 1
                    rep_occupy[rep_occupy.index(i)] = -1
                    customer[i] = 2000
        rep_temp.sort()
        rep_waiting.extend(rep_temp)
        rec = list()
        for person in rec_waiting:
            for i in range(N):
                if rec_occupy[i] == -1:
                    rec_occupy[i] = person
                    customer[person] = reception[i]
                    status[person] += 1
                    rec.append(person)
                    if i == A:
                        visit_A[person] = True
                    break
        while rec:
            r = rec.pop()
            rec_waiting.remove(r)
        rep = list()
        for idx, person in rep_waiting:
            for i in range(M):
                if rep_occupy[i] == -1:
                    rep_occupy[i] = person
                    customer[person] = repair[i]
                    status[person] += 1
                    rep.append((idx, person))
                    if i == B:
                        if visit_A[person]:
                            result += person+1
                    break
        while rep:
            r = rep.pop()
            rep_waiting.remove(r)

    if result == 0:
        result = -1
    print(f'#{tc} {result}')