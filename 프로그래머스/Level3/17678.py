# 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    timetable.sort()

    cur_hour = 9
    cur_minute = 0
    answer_hour = 0
    answer_minute = 0
    for i in range(n):
        # print(cur_hour, cur_minute)
        # print(timetable)
        count = 0
        max_hour = cur_hour
        max_minute = answer_minute
        for j in range(m):
            if len(timetable) == 0:
                break

            hour, minute = map(int, timetable[0].split(":"))

            if cur_hour > hour or (cur_hour == hour and cur_minute >= minute):
                timetable.pop(0)
                max_hour = hour
                max_minute = minute
                count += 1
            else:
                break

            if count >= m:
                break
        # print(count)
        if count < m:
            answer_hour = cur_hour
            answer_minute = cur_minute
        else:
            answer_hour = max_hour
            answer_minute = max_minute - 1
            if answer_minute == -1:
                answer_hour -= 1
                answer_minute = 59

        # 다음 셔틀 시간
        cur_hour += (cur_minute + t) // 60
        cur_minute = (cur_minute + t) % 60

    if answer_hour >= 10:
        answer_hour = str(answer_hour)
    else:
        answer_hour = '0' + str(answer_hour)
    if answer_minute >= 10:
        answer_minute = str(answer_minute)
    else:
        answer_minute = '0' + str(answer_minute)

    answer = answer_hour + ':' + answer_minute
    print(answer)
    return answer


solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
solution(2, 10, 2, ["09:10", "09:09", "08:00"])
solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])
solution(1, 1, 1, ["23:59"])
solution(10, 60, 45,
         ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
          "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
