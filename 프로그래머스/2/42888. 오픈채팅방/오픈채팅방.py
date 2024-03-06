def solution(record):

    # uuid 사용자의 들어옴, 나감 상태기록
    entry = dict()
    # uuid 사용자의 이름 기록
    nickname = dict()
    
    # [uuid, 입/출]
    ans = []
    
    for s in record:
        # "Enter uid1234 Muzi"
        r = list(s.split())

        if r[0] == "Enter":
            e, u, n = r[0], r[1], r[2]
            ans.append([u, e])
            entry[u] = e
            nickname[u] = n
        elif r[0] == "Leave":
            e, u = r[0], r[1]
            ans.append([u, e])
            entry[u] = e
        elif r[0] == "Change":
            u, n = r[1], r[2]
            nickname[u] = n
    
    '''
    [["uid1234","Enter"],
     ["uid4567","Enter"],
     ["uid1234","Leave"],
     ["uid1234","Enter"]]
    '''
    ans_msg = []
    for a in ans:
        u, e = a[0], a[1]
        if e == "Enter":
            message = nickname[u] + "님이 들어왔습니다."
            ans_msg.append(message)
        elif e == "Leave":
            message = nickname[u] + "님이 나갔습니다."
            ans_msg.append(message)
    
    return ans_msg