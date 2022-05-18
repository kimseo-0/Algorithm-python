# 길찾기 게임
# https://programmers.co.kr/learn/courses/30/lessons/42892
import heapq
import sys
sys.setrecursionlimit(10**6)

def binary(array, answer, start, end):
    # print(array[start:end + 1], answer)
    if start > end:
        return 0
    if start == end:
        answer[0].append(array[start][2])
        answer[1].append(array[start][2])
        return 0

    new_array = array[start:end + 1]
    heapq.heapify(new_array)
    [_, _, num, max_index] = heapq.heappop(new_array)
    answer[0].append(num)

    binary(array, answer, start, max_index - 1)
    binary(array, answer, max_index + 1, end)

    answer[1].append(num)

def solution(nodeinfo):
    answer = [[], []]

    for i in range(len(nodeinfo)):
        nodeinfo[i] = [-nodeinfo[i][1], nodeinfo[i][0], i + 1]

    nodeinfo.sort(key=lambda x: x[1])

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i)

    binary(nodeinfo, answer, 0, len(nodeinfo) - 1)
    print(answer)

    return answer


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
