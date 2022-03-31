def merge_sort(lst):
    # M = len(lst) - 1
    # left = game(lst[:M // 2 + 1])
    # right = game(lst[M // 2 + 1:])

    # middle = len(lst) // 2
    # middle = (len(lst) - 1) // 2 + 1

    # lst 반으로 나누기
    if len(lst)==1:
        return lst
    mid_i = (len(lst) -1)//2 + 1
    left = lst[:mid_i]
    right = lst[mid_i:]
    # 한명씩 비교하기 위함
    left = merge_sort(left) # 1
    right = merge_sort(right) # 2
    return merge(left, right)


def merge(left, right):
    left = [lst[left[0]]]
    right = [lst[right[0]]]
    result = []
    left_l = right_l = 0
    i = j = 0
    if left:
        left_l = len(left)
    if right:
        right_l = len(right)
    while left_l>i or right_l>j: # 둘중 하나라도 있을때
        # 둘 다 있을때
        if left_l>i and right_l>j:
            if left[i] == right[j]:
                result.append(left[i])
            elif left[i] !=3 and right[j] != 3: # 1, 2(2승리)
                result.append(max(left[i], right[j]))
            elif left[i] !=1 and right[j] !=1: # 둘다 1이 아닐때
                result.append(max(left[i], right[j]))
            else:  # 1, 3 (1승리)
                result.append(min(left[i], right[j]))
            i += 1
            j += 1
        else: # 하나만 있을때
            if left_l>i: # left가 있음
                result.append(left[i])
                i += 1
            else: #right가 있음
                result.append(right[j])
                j += 1
    return result





t = int(input())
for tc in range(1, t+1):
    N = int(input()) # 인원수
    lst = list(map(int, input().split()))
    card = [x for x in range(N)]
    res = merge_sort(card)


    print(f'#{tc} {res}')