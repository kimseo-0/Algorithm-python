# 이분탐색 > 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

import heapq

# 틀린 풀이 : 시간초과 발생
def solution(n, times):
    space_num = len(times)
    space = []
    for i in range(space_num):
        heapq.heappush(space, (times[i], times[i]))     # (이제까지 이자리에서 심사를 진행한 시간, 이 자리에서 심사하하는데 걸리는 시간)

    time = 0
    while n > 0:
        (all_time, current_time) = heapq.heappop(space)
        n -= 1
        time += (all_time - time)

        heapq.heappush(space, (all_time + current_time, current_time))

    return time

# 정답 : 이분 탐색 풀이
def solution1(n, times):
    start = 0
    end = max(times) * n
    answer = end

    while True:
        if start > end:
            break

        check_people = 0
        mid = (start + end) // 2
        for time in times:
            check_people += (mid // time)

        if check_people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(solution(6, [7, 10]))
print(solution1(6, [7, 10]))
