lst = [int(input()) for _ in range(9)]

lst.sort()
 #[7, 8, 10, 13, 15, 19, 20, 23, 25]


flag = 0
for i in range(9): # 0-8
    alst = lst[:]
    alst.pop(i)
    for j in range(8): # 0-7
        blst = alst[:]
        blst.pop(j)
        if sum(blst)==100:    # and len(alst)==7:
            flag = 1
            print(blst)
            break
    if flag:
        break