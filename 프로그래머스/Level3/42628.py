# 이중 우선순위 큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq
from heapq import heappush, heappop


def solution(operations):
    max_h = []
    min_h = []
    num_list = []

    for op in operations:
        [action, num] = op.split()

        if action == 'I':
            heapq.heappush(max_h, (-int(num), len(num_list)))
            heapq.heappush(min_h, (int(num), len(num_list)))
            num_list.append(int(num))
        elif action == "D":
            if num == "1":
                if len(max_h) == 0:
                    continue
                (_, index) = heapq.heappop(max_h)
                num_list[index] = "x"
            elif num == "-1":
                if len(min_h) == 0:
                    continue
                (_, index) = heapq.heappop(min_h)
                num_list[index] = "x"

            if len(max_h) == 0 or len(min_h) == 0 or -max_h[0][0] < min_h[0][0]:
                max_h = []
                min_h = []

    num_list = list(filter(lambda x: x != "x", num_list))
    if len(num_list) == 0:
        return [0, 0]
    elif len(num_list) == 1:
        return [num_list[0], num_list[0]]
    else:
        (max_num, _) = heapq.heappop(max_h)
        (min_num, _) = heapq.heappop(min_h)
        return [-max_num, min_num]


# solution(["I 16","D 1"])
# solution(["I 7","I 5","I -5","D -1"])
# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]))
# solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))


def solution1(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]


# print(solution1(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]))