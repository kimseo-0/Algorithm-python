# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    left_truck_num = len(truck_weights)
    sum_of_weight = truck_weights[0]
    queue = [*[0] * (bridge_length - 1), truck_weights.pop(0)]

    time = 1
    while queue or len(truck_weights) > 0:
        time += 1
        sum_of_weight -= queue[0]

        if queue.pop(0) > 0:
            left_truck_num -= 1

        if left_truck_num <= 0:
            break

        if len(truck_weights) <= 0:
            continue

        if sum_of_weight + truck_weights[0] <= weight:
            sum_of_weight += truck_weights[0]
            queue.append(truck_weights.pop(0))
        else:
            queue.append(0)

    print(time)
    return time


solution(2, 10, [7, 4, 5, 6])
