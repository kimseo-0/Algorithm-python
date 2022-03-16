# 무지의 먹방 라이브
# 그리디 기준 : 해당 음식을 먹는데 걸리는 시간이 짧은 순서대로

# 우선순위큐가 필요할때, NlogN을 보장하며 오름차순 또는 내림차순 정렬이 피료한 경우 사용
import heapq
import sys
input = sys.stdin.readline

# 시간초과
def solution(food_times, k):
    N = len(food_times)
    index = 0
    time = 0
    if k + 1 <= N:
        return k + 1

    while time < k + 1:
        if food_times[index] != 0:
            food_times[index] -= 1
            time += 1

        index = (index + 1) % N
    return index

# 시간초과
def solution1(food_times, k):
    n = len(food_times)
    food_index = [i for i in range(n)]
    index = 0
    time = 0
    if k + 1 <= n:
        return k + 1

    while time < k:
        food_times[food_index[index]] -= 1
        if food_times[food_index[index]] == 0:
            result = food_index.pop(index)
            if len(food_index) == 0:
                return result
            index = index % len(food_index)
        else:
            index = (index + 1) % len(food_index)
        time += 1

    return food_index[index] + 1

# 정답
def solution2(food_times, k):
    # 방송이 다시 시작한 후 다시 먹을 음식이 없는 경우 바로 종료
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    sort_food_times = []
    for i in range(n):
        heapq.heappush(sort_food_times, (food_times[i], i + 1))
    # sort_food_times.sort()

    time = 0    # 지금까지 먹은 음식들의 총 시간
    previous_food_time = 0  # 바로 이전에 다 먹은 음식의 시간
    while True:
        if time + (sort_food_times[0][0] - previous_food_time) * n > k:
            break
        (food_time, i) = heapq.heappop(sort_food_times)
        time += (food_time - previous_food_time) * n
        n -= 1
        previous_food_time = food_time

    # 남은 음식들을 번호 순서대로 다시 정렬
    sort_food_times.sort(key=lambda x: x[1])

    # 남은 음식들 중 남은 시간만큼
    return sort_food_times[(k - time) % n][1]


print(solution2([3, 1, 2], 5))
# print(solution1([3, 1, 1], 5))
# print(solution2([4, 3, 4, 1, 3], 9))
