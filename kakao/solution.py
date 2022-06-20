import sys
sys.stdin = open('sample_input.txt', encoding='UTF-8')

SCALE = {
    '도' : 1, '레': 2, '미': 3, '파': 4, '솔': 5, '라': 6, '시': 7
}
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    notes = input().split()

    result = 0
    idx = 0
    repeat = 0  # 되돌아갈 도돌이표가 있는 인덱스 저장
    skip = -1   # 도돌이표로 되돌아간 뒤, 도돌이표가 다시 실행되지 않도록 하기위한 인덱스 저장
    while idx < N:
        note = notes[idx]
        cursor = 0
        if idx == skip: # skip 인덱스면 더이상 연산하지 않고 다음 인덱스로 진행
            idx += 1
            continue
        if note[cursor] == '|': # 도돌이표 시작지점일 경우, 인덱스를 repeat에 저장
            repeat = idx
            idx += 1
            continue
        elif note[cursor] == ':':
            skip = idx
            idx = repeat
            continue

        while note[cursor] == '옥':
            cursor += 1
        point = cursor*7 + SCALE[note[cursor]]
        cursor += 1
        if note[cursor] == '#':
            point += 0.5
            cursor += 1
        elif note[cursor] == 'b':
            point -= 0.5
            cursor += 1

        dot = 1
        if note[cursor] == '.':
            dot = 1.5
            cursor += 1
        beat = int(note[cursor:])

        point = point * beat * dot
        result += point
        idx += 1

    print(f'#{tc} {result:.1f}')