# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):

    # 더이상 나갈 트럭이 없는 상황에서 남은 0 값들을 제거할 때 낭비되는 시간을 줄이기 위해
    # 모든 트럭이 나갔는지 확인할 수 있는 남은 트럭 수 변수 생성
    left_truck_num = len(truck_weights)

    # 파이썬 sum 을 사용하면 O(N) 이 걸리기 때문에
    # 현재 다리위에 있는 모든 트럭의 무게의 합을 저장하는 변수 생성
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
