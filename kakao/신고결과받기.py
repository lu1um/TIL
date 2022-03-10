def solution(id_list, report, k):
    ids = dict()
    for id in id_list:
        ids[id] = [[], 0]
    for repo in report:
        accuser, defendant = repo.split()
        if accuser in ids[defendant][0]:
            continue
        else:
            ids[defendant][0].append(accuser)
            ids[defendant][1] += 1
    mail_count = [0] * len(id_list)
    for reported in ids.values():
        if reported[1] >= k:
            for i in range(len(id_list)):
                if id_list[i] in reported[0]:
                    mail_count[i] += 1
    return mail_count