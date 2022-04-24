import sys
sys.stdin = open('input.txt')

STATE_ROOM = 0
STATE_WAIT = 1
STATE_STAIR = 2
STATE_FINISH = 3
MAX_TIME = 10*20*10

def makeCase(M, i=0, case=[]):
    global cases
    if i == M:
        cases.append(case)
        return
    makeCase(M, i+1, case+[0])
    makeCase(M, i+1, case+[1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    people = list()
    stairs = list()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append((i, j))
            elif arr[i][j] != 0:
                stairs.append((i, j, arr[i][j]))

    distance = list()
    for person in people:
        pr, pc = person
        dis = list()
        for sr, sc, _ in stairs:
            dis.append(abs(pr-sr)+abs(pc-sc))
        distance.append(dis)

    cases = list()
    people_number = len(people)
    makeCase(people_number)

    min_time = MAX_TIME
    for case in cases:
        state = [STATE_ROOM] * people_number
        people_time = [0] * people_number
        for i in range(people_number):
            people_time[i] = distance[i][case[i]]

        time = 0
        stair_occupy = [0, 0]
        while sum(state) < people_number * STATE_FINISH:
            move_time = min(people_time)
            waiting = list()
            for i in range(people_number):
                people_time[i] -= move_time
                if people_time[i] <= 0:
                    if state[i] == STATE_WAIT:
                        waiting.append(i)
                    elif state[i] == STATE_STAIR:
                        state[i] += 1
                        stair_occupy[case[i]] -= 1
                        people_time[i] = MAX_TIME
                    elif state[i] == STATE_ROOM:
                        state[i] += 1
                        people_time[i] = 1
            for i in waiting:   # 순서대로 확인하지말고, 다 내려간사람부터 먼저 occupy를 해제해주자.
                if stair_occupy[case[i]] < 3:
                    state[i] += 1
                    stair_occupy[case[i]] += 1
                    people_time[i] = stairs[case[i]][2]
                else:
                    people_time[i] = 1
            time += move_time
        if time < min_time:
            min_time = time
    print(f'#{tc} {min_time}')

