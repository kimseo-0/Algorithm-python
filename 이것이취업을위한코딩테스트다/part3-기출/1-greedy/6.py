import heapq
import sys
input = sys.stdin.readline


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

def solution2(food_times, k):
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    sort_food_times = []
    for i in range(n):
        heapq.heappush(sort_food_times, (food_times[i], i + 1))
    sort_food_times.sort()

    time = 0
    previous_food_time = 0
    while True:
        if time + (sort_food_times[0][0] - previous_food_time) * n > k:
            break
        (food_time, i) = heapq.heappop(sort_food_times)
        time += (food_time - previous_food_time) * n
        n -= 1
        previous_food_time = food_time
        print(time)

    sort_food_times.sort(key=lambda x: x[1])

    return sort_food_times[(k - time) % n][1]


# print(solution([3, 1, 1], 5))
# print(solution1([3, 1, 1], 5))
print(solution2([4, 3, 4, 1, 3], 9))
