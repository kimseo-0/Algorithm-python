# 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    user = {}

    for i in record:
        line = i.split()

        if line[0] != "Leave":
            user[line[1]] = line[2]

    for i in record:
        line = i.split()

        if line[0] == "Enter":
            answer.append(user[line[1]] + "님이 들어왔습니다.")
        elif line[0] == "Leave":
            answer.append(user[line[1]] + "님이 나갔습니다.")

    return answer


a = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(a)
