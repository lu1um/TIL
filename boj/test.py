from collections import deque
N, M = map(int, input().split())
vmap = [list(map(int, input().split())) for _ in range(N)]
di = [1, -1, 0, 0, 1, 1, -1, -1]
dj = [0, 0, 1, -1, 1, -1, 1, -1]
virus = []
candidate = []

for i in range(N):
    for j in range(M):
        if vmap[i][j] == 2:
            virus.append(M * i + j)
        elif vmap[i][j] == 0:
            candidate.append(M * i + j)
area = len(candidate)   # 0의 갯수
answer = 0
min_cnt = N*M
for i in range(area-2):
    for j in range(i+1, area-1):
        for k in range(j+1, area):
            ok = 0
            tmp_cnt = 3
            visit = [0]*(N*M)
            que = deque(virus)
            tmp_wall = {candidate[i], candidate[j], candidate[k]}
            visit[candidate[i]] = visit[candidate[j]] = visit[candidate[k]] = 1
            for wall in tmp_wall:
                chk = 0
                wi = wall // M
                wj = wall % M
                for d in range(8):
                    nw = wall + M*di[d] + dj[d]
                    nwi = wi + di[d]
                    nwj = wj + dj[d]
                    if 0 <= nwi < N and 0 <= nwj < M and vmap[nwi][nwj] == 1:
                        chk += 1
                    elif nwi < 0 or nwi >=N or nwj < 0 or nwj >= M:
                        chk += 1
                    elif nw in tmp_wall:    # 가장자리인지, 주변에 벽이 있는지
                        chk += 1
                if chk < 2:
                    break
            else:
                ok = 1
            if ok == 0:
                continue
            while que:
                if tmp_cnt > min_cnt:
                    break
                v = que.popleft()
                si = v//M
                sj = v%M
                for d in range(4):
                    nv = v + M*di[d] + dj[d]
                    ni = si + di[d]
                    nj = sj + dj[d]
                    if 0 <= ni < N and 0 <= nj < M and visit[nv] == 0 and vmap[ni][nj] == 0:
                        que.append(nv)
                        visit[nv] = 1
                        tmp_cnt += 1
            else:
                if tmp_cnt < min_cnt:
                    min_cnt = tmp_cnt
                if area - tmp_cnt > answer:
                    answer = area - tmp_cnt
print(answer)