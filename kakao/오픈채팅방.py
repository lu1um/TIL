def solution(record):
    chat = list()
    user = dict()
    for re in record:
        r = list(re.split())
        if r[0] == 'Enter':
            chat.append((r[1], 0))
            user.update({r[1]: r[2]})
        elif r[0] == 'Leave':
            chat.append((r[1], 1))
        else:
            user.update({r[1]: r[2]})
    answer = list()
    for c in chat:
        if c[1] == 0:
            answer.append(f'{user[c[0]]}님이 들어왔습니다.')
        else:
            answer.append(f'{user[c[0]]}님이 나갔습니다.')
    return answer