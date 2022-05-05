def solution(n, k, cmd):
    answer = ['O'] * n
    pre = list(range(-1, n-1))
    nxt = list(range(1, n)) + [-1]
    deleted = []
    cursor = k
    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                cursor = pre[cursor]
        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                cursor = nxt[cursor]
        elif c == 'C':
            answer[cursor] = 'X'
            deleted.append(cursor)
            nxt[pre[cursor]] = nxt[cursor]
            pre[nxt[cursor]] = pre[cursor]
            if nxt[cursor] == -1:
                cursor = pre[cursor]
            else:
                cursor = nxt[cursor]
        else:
            undo = deleted.pop()
            answer[undo] = 'O'
            nxt[pre[undo]] = undo
            pre[nxt[undo]] = undo
    answer = ''.join(answer)
    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))